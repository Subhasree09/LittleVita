from django.shortcuts import render, redirect
from .forms import SignUpForm, VaccineStatusForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import openai
import google.generativeai as genai
from django.http import JsonResponse
from .models import Parent, Child, Disease, Doctor, Nutrition, Vaccine, VaccineStatus, Review, Hospital
from decouple import config
from datetime import date, datetime
import json

# Set the Gemini API key
GOOGLE_API_KEY=config('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


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
    
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@login_required(login_url='login')
def dashboard(request):
    context={}
    context['activeDashboard']='activate'
    if request.user.is_authenticated:
        print("user is authenticated")
        if request.method == 'POST':
            if 'hide' in request.POST and request.POST['hide'] == 'child_add':
                print("child add")
                child_name = request.POST.get('child_name')
                child_sex = request.POST.get('sex')
                date_of_birth = datetime.strptime(request.POST.get('dob'), '%Y-%m-%d').date()
                parent = Parent.objects.get(user=request.user)
                today = date.today()
                age = age = calculate_age(date_of_birth)
                print(age)
                child = Child.objects.create(child_name=child_name, child_sex=child_sex, date_of_birth=date_of_birth, age=age, parent=parent)
                child.save()
                messages.success(request, 'Child added successfully')
                return redirect('dashboard')
            
            else:
                print("vaccine status")
                parent = Parent.objects.get(user=request.user)
                form = VaccineStatusForm(request.POST, user=parent)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Vaccine status updated successfully')
                    return redirect('dashboard')
                else:
                    print(form.errors)
                    messages.error(request, 'Invalid form data. Try again!')
                    return redirect('dashboard')
        
        parent = Parent.objects.get(user=request.user)
        context['parent'] = parent

        children = Child.objects.filter(parent=parent)
        for child in children:
            vaccine_statuses = VaccineStatus.objects.filter(child=child, completed=True)
            child.vaccines_taken = [status.vaccine for status in vaccine_statuses]
            
            # Fetch all vaccines
            all_vaccines = Vaccine.objects.all()

            # Exclude the vaccines that the child has taken
            child.vaccines_not_taken = all_vaccines.exclude(vaccine_id__in=[vaccine.vaccine_id for vaccine in child.vaccines_taken])

        context['children']=children


        vaccine_status_form = VaccineStatusForm(request.POST or None, user=parent)
        context['vaccine_status'] = vaccine_status_form
        
        return render(request, 'Base/dashboard.html', context)
    else:
        messages.error(request, 'You are not logged in')
        return redirect('login')

def home(request):
    context={}
    context['activeHome']='activate'
    answer = "Hi, Mom! I am here to help you. Ask me anything."
    context['answer'] = answer
    if request.method == "POST":
        ask = request.POST.get('question')
        response = model.generate_content(f"""
                I am an AI developed for a website named LittleVita, a platform dedicated to managing children's vaccination schedules and providing information about newborn baby health. 
                I can provide information about adding children, managing their vaccination schedules, tracking their vaccination status, and searching for information about nutrition, diseases, doctors, and vaccines specifically for newborn babies. 
                I can help you find doctors and hospitals Who are not associated with our platform, LittleVita. 
                However, I can't provide information that is not related to our website or newborn baby healthcare. 
                User's question: {ask}
                """)
        print(response.text)

        # print(completion)
        answer = (response.text)
        context['answer'] = answer
        context['ask'] = ask 
        return JsonResponse({'answer': answer})


    return render(request, 'Base/home.html',  context)

def nutrition(request):
    context={}
    context['activeNutrition']='activate'
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
    context={}
    context['activeAwarness']='activate'
    return render(request, 'Base/awarness.html', context)

def blog(request):
    context={}
    context['activeBlog']='activate'
    return render(request, 'Base/blog.html', context)

def feedback(request):
    context={}
    context['activeFeedback']='activate'
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in')
            return redirect('login')
        else:
            message = request.POST.get('message')
            ratings = int(request.POST.get('rate'))
            user_rating = Review.objects.create(user=request.user, rating=ratings, review=message)
            user_rating.save()
            messages.success(request, 'Feedback submitted successfully')
            return redirect('feedback')
    else:
        reviews = Review.objects.all()
        context['reviews'] = reviews
        
        return render(request, 'Base/feedback.html', context)

def doctors(request):
    context={}
    context['activeDoctors']='activate'
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
    context={}
    context['activeDisease']='activate'
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
    context['diseases'] = diseases



    return render(request, 'Base/disease.html', context)

def vaccine(request):
    context={}
    context['activeVaccine']='activate'
    vaccines= Vaccine.objects.all()
    context = {'vaccines':vaccines}
    return render(request, 'Base/vaccine.html', context)

def vaccine_schedule(request):
    context={}
    context['activeVaccine']='activate'
    return render(request, 'Base/vaccine_schedule.html', context)

# def videos(request):
#     return render(request, 'Base/videos.html')


def hospital(request):
    context={}
    context['activeHospital']='activate'
    if request.method == 'GET':
        if 'q' in request.GET:
            q = request.GET['q']

            # access hospital from database and filter it with the query
            hospital = Hospital.objects.filter(hospital_name__icontains=q)
            city = Hospital.objects.filter(city__icontains=q)
            hospitals = hospital.union(city)
    
            # access hospital from gemini api 
            response = model.generate_content(f"""
                generate hospitals information for {q} in a json format.
                The information must contain hospital_name, address, phone_number".
                Do not write  any other information such as json or python and so on.
                only write the information in json string  format so that i can easily convert json to python dict.
                """)
            print(response.text)
            # print(type(response.text))

            gemini_hospitals = json.loads(response.text)
            first_key = list(gemini_hospitals.keys())[0]
            gemini_hospitals = gemini_hospitals[first_key]

            print(gemini_hospitals)
            # print(type(gemini_hospitals))

            if hospitals.count() == 0 and len(gemini_hospitals) == 0:
                messages.error(request, 'No results found')
            else:
                context['hospitals'] = hospitals
                context['gemini_hospitals'] = gemini_hospitals
                return render(request, 'Base/hospital.html', context)
            
        
    hospital = Hospital.objects.all()
    context['hospitals'] = hospital
    return render(request, 'Base/hospital.html', context)