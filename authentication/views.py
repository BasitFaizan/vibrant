from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Projects.models import Projectcard,ProjectBlog
from Projects.forms import ProjectBlogForm
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.
def home(request):
    productCardDetails = Projectcard.objects.all()
    instaLinks = ['https://www.instagram.com/mdshaad783/','https://www.instagram.com/basit.ig/']
    return render(request,'index.html',{'productCardDetails':productCardDetails})

def about(request):
    return render(request,'about.html')
    
def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        # phoneNumber = request.POST.get('phoneNumber')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Your password and confirm password do not match.......Account not created")
        else:
            my_user =User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')


def loginUser(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            
            login(request, user)
        # Redirect to a success page.
            return redirect('home')
        else:
        # Return an 'invalid login' error message.
            return HttpResponse("Username or Password do not match !!!!")

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")

def explore(request,projectId):
    projectDetail2 = get_object_or_404(Projectcard, pk=projectId)
    projectDetail = Projectcard.objects.filter(pk=projectId)
    user = request.user
    if request.method == "POST":
        ProjectBlogName = request.POST.get('ProjectBlogName')
        project_blog_image = request.FILES.get('ProjectBlogImage')
        newProjectBlogPost = ProjectBlog.objects.create(
            projectCateg=projectDetail2,
            authorName=user,
            blogTitle=ProjectBlogName,
            projectTitleImage=project_blog_image  # Use the correct field name
        )
    
    projectBlogPost = ProjectBlog.objects.filter(projectCateg=projectDetail2)
    return render (request,"explore.html",{'projectDetail':projectDetail,'projectBlogPost':projectBlogPost})

def view_project_blog(request,projectBlogId):
    projectBlogPost = get_object_or_404(ProjectBlog, pk=projectBlogId)
    form = ProjectBlogForm(initial={
        'blogTitle': projectBlogPost.blogTitle,
        'projectTitleImage': projectBlogPost.projectTitleImage,
        'content':projectBlogPost.content,
    })
    return render(request,'projectBlog.html',{'form':form})