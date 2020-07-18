from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post

# Create your views here.


def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html',context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 7 or len(phone) < 10 or len(content) < 7:
            messages.error(request, 'Please fill the form correctly !! ')

        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, 'You have submitted your form successfully!! ')
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET['query']
    # if len(query)>78:
    #     posts=[]
    # else:
    #     posts=Post.objects.filter(title__icontains=query)

    # if posts.count()==0:
    #      messages.error(request, 'No Search result found please refine your query!!')
    postsTitle = Post.objects.filter(title__icontains=query)
    postsContent = Post.objects.filter(content__icontains=query)
    posts = postsTitle.union(postsContent)
    if posts.count() == 0:
        messages.warning(
            request, 'No Search result found please refine your query!!')
    context = {'posts': posts, 'query': query}
    return render(request, 'home/search.html', context)


def handelSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if len(username) > 20:
            messages.error(request, 'Username contain atmost 10 characters !!')
            return redirect('/')
        if not username.isalnum():
            messages.error(
                request, 'Username contains alphabets and letters only!!')
            return redirect('/')
        if password != cpassword:
            messages.error(request, 'Passwords does not matches !!')
            return redirect('/')

        myUser = User.objects.create_user(username, email, password)
        myUser.first_name = name
        myUser.last_name = lname
        myUser.save()
        messages.success(
            request, 'Your Account has been created successfully!!')
        return redirect('/')

    else:
        return HttpResponse('404-Not Found')


def user_login(request):
    if request.method == 'POST':
        loginUsername = request.POST['loginUsername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginUsername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully Logged In!!')
            return redirect('/')

        else:
            messages.error(request, 'Invalid credentials Please try again !!')
            return redirect('/')
    return HttpResponse('404-Not Found')


def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully Logged Out!!')
    return redirect('/')
