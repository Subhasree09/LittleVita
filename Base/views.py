from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import openai
from django.http import JsonResponse
from .models import Parent, Child, Disease, Doctor, Nutrition, Vaccine
from decouple import config

# Create your views here.
def loginUser(request):
    context = {}

    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('home')
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print("authenticating")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('dashboard')
            else:
                print('Invalid username or password')
                messages.error(request, 'Invalid username or password')
                return redirect('login')
        else:
            messages.error(request, 'Invalid form Data. Try again!')
            return redirect('login')
            
    form = AuthenticationForm()
    context['form'] = form            
    return render(request, 'Base/login.html', context)

def signupUser(request):
    context={}
   
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            parent= Parent.objects.create(user=user, first_name=user.first_name, last_name=user.last_name, email=user.email, phone_number=form.cleaned_data['phone_number'])
            parent.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Something Error occured. Try again!')
            return redirect('signup')
        
    form=SignUpForm()
    context['form']=form
    return render(request, 'Base/signup.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    context={}
    if request.user.is_authenticated:
        if request.method == 'POST':
            print("data collecting")
            child_name = request.POST.get('child_name')
            child_sex = request.POST.get('sex')
            date_of_birth = request.POST.get('dob')
            parent = Parent.objects.get(user=request.user)
            child = Child.objects.create(child_name=child_name, child_sex=child_sex, date_of_birth=date_of_birth, parent=parent)
            child.save()
            messages.success(request, 'Child added successfully')
            return redirect('dashboard')
        
        parent = Parent.objects.get(user=request.user)
        # children = Child.objects.filter(parent=parent)
        context['parent'] = parent


        return render(request, 'Base/dashboard.html', context)
    else:
        messages.error(request, 'You are not logged in')
        return redirect('login')

def home(request):

    answer = "Hi, Mom! I am here to help you. Ask me anything."
    context = {'answer':answer}
    if request.method == "POST":
        ask = request.POST.get('question')
        API_KEY = config('API_KEY')
        openai.api_key = API_KEY

        completion = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=ask,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # print(completion)
        answer = (completion.choices[0].text)
        context = {'answer':answer, 'ask':ask}
        return JsonResponse({'answer': answer})

    return render(request, 'Base/home.html')

def nutrition(request):
    context={}
    if request.method == 'GET':
        if 'q' in request.GET:
            q = request.GET['q']
            nutrition = Nutrition.objects.filter(nutrition_name__icontains=q)
            nutrition_desc = Nutrition.objects.filter(description__icontains=q)
            nutritions = nutrition.union(nutrition_desc)
            if nutritions.count() == 0:
                messages.error(request, 'No results found')
            else:
                context['nutritions'] = nutritions
                return render(request, 'Base/nutrition.html', context)
    nutritions = Nutrition.objects.all()
    context['nutritions'] = nutritions
    return render(request, 'Base/nutrition.html', context)

def awarness(request):
    return render(request, 'Base/awarness.html')

def blog(request):
    return render(request, 'Base/blog.html')

def contact(request):
    return render(request, 'Base/contact.html')

def doctors(request):
    context={}

    if request.method == 'GET':
        if 'q' in request.GET:
            q = request.GET['q']
            doctor = Doctor.objects.filter(doctor_name__icontains=q)
            specialization = Doctor.objects.filter(specialization__icontains=q)
            hospital = Doctor.objects.filter(hospital__icontains=q)
            doctors = doctor.union(specialization, hospital)
            if doctors.count() == 0:
                messages.error(request, 'No results found')
            else:
                context['doctorsList']=doctors
                return render(request, 'Base/doctors.html', context)
            
    doctorsList= Doctor.objects.all()
    context['doctorsList']=doctorsList
    return render(request, 'Base/doctors.html', context)

def disease(request):

    if request.method == 'GET':
        if 'q' in request.GET:
            q = request.GET['q']
            disease = Disease.objects.filter(disease_name__icontains=q)
            disease_desc = Disease.objects.filter(description__icontains=q)
            symptoms = Disease.objects.filter(symptoms__icontains=q)
            diseases = disease.union(disease_desc, symptoms)

            if diseases.count() == 0:
                messages.error(request, 'No results found')
            else:
                context = {'diseases':diseases}
                return render(request, 'Base/disease.html', context)
    diseases = Disease.objects.all()
    context = {'diseases':diseases}



    return render(request, 'Base/disease.html', context)

def vaccine(request):
    return render(request, 'Base/vaccine.html')

def vaccine_schedule(request):
    return render(request, 'Base/vaccine_schedule.html')

# def videos(request):
#     return render(request, 'Base/videos.html')

