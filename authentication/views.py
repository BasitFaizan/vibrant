from django.shortcuts import render

# Create your views here.
def home(request):
    instaLinks = ['https://www.instagram.com/mdshaad783/','https://www.instagram.com/basit.ig/']
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')