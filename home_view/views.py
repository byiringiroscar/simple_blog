from django.shortcuts import render


# Create your views here.

def home_blog(request):
    return render(request, 'home_temp/home_blog.html')
