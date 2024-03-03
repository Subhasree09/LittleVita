from django.shortcuts import render

# Create your views here.
def home(request):
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

def login(request):
    return render(request, 'Base/login.html')

def signup(request):
    return render(request, 'Base/signup.html')