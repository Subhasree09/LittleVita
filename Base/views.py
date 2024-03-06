from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import openai
from django.http import JsonResponse
from .models import Parent, Child
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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
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
    return render(request, 'Base/nutrition.html')

def awarness(request):
    return render(request, 'Base/awarness.html')

def blog(request):
    return render(request, 'Base/blog.html')

def contact(request):
    return render(request, 'Base/contact.html')

def doctors(request):
    return render(request, 'Base/doctors.html')

def disease(request):
    return render(request, 'Base/disease.html')

def vaccine(request):
    return render(request, 'Base/vaccine.html')

def videos(request):
    return render(request, 'Base/videos.html')

