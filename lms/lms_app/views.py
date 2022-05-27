from lms_app.decorators import unauthenticated_user
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm, UsernameField
from django.shortcuts import render, redirect
from .models import *
from .forms import AdminSignUpForm, BookForm, LoginAdminForm
from .forms import SignUpForm, CreateUserForm,EditProfileForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages, auth
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, context
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .decorators import allowed_users, unauthenticated_user

########   Home page   ###### 
# @unauthenticated_user
def home(request):
    return render(request,'pages/home.html')

#######   signUP page   #######
def signUP(request):
    return render(request,'pages/signUP.html')

########   Admin Registration   ###########
@unauthenticated_user
def registerAdmin(request):
    user_creation_form = CreateUserForm()
    if request.method == 'POST':
        user_creation_form = CreateUserForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save()
            group = Group.objects.get(name = 'admin')
            user.groups.add(group)
            return redirect('loginUser')
    context = {'AdminSF':user_creation_form}

    return render(request,'pages/registerAdmin.html', context)

########   User Registration   ###########
@unauthenticated_user
def registerUser(request):
    
    user_creation_form = CreateUserForm()
    if request.method == 'POST':
        user_creation_form = CreateUserForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save()            
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            return redirect('loginUser')
    context = {
        'user_creation_form': user_creation_form
    }
    return render (request, 'pages/registerUser.html', context)

#######   AdminLogin   ###########
"""
@unauthenticated_user
def Loginadmin(request): 
    try:        
        if request.method == 'POST':        
            email = request.POST['email']
            password = request.POST['password']
            isFound = SignUpAdmin.objects.get(Email = email , password = password)
            print('it is POST')
            if isFound:
                print ('it is found')
                return redirect('homeeAdmin')
    except ObjectDoesNotExist:
        messages.info(request,'user name or password is incorrect')
        return redirect('loginAdmin')
    return render(request, 'pages/loginAdmin.html')  
"""

######    login    ##########
@unauthenticated_user
def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)            
        print("it is POST")
        if user is not None:                
            print("it is found")
            login(request, user)
            if user.groups.filter(name = 'customer'):
                return redirect('homeeUser')
            if user.groups.filter(name = 'admin'):
                return redirect('homeeAdmin')
        else:
            messages.info(request,'user name or password is incorrect')
            
    return render(request,'pages/loginUser.html')

#########  logout  #############
def logoutUser(request):
    logout(request)
    return redirect ('home')

#########  User Home   ##########
@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['admin','customer'])
def homeeUser(request):
    return render(request,'pages/homeeUser.html')

#########   Admin Home   #########
@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['admin'])
def homeeAdmin(request):
    return render(request,'pages/homeeAdmin.html')

#####    profile   ######
def profile(request):
    context = {'user': request.user}
    return render(request,'pages/profile.html', context)

#####    Edit Profile    ############
def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid:
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance = request.user)
        context = {'editForm':form}
        return render(request, 'pages/editProfile.html', context)

######    books   ###########    
@login_required(login_url='loginAdmin')
@allowed_users(allowed_roles=['admin','customer'])
def books(request):
    context = {
        'books':addBooks.objects.all(),
    }  
    return render(request,'pages/books.html',context)

######    bookView   ##############
@login_required(login_url='loginAdmin')
@allowed_users(allowed_roles=['admin','customer'])
def bookView(request, id):
    context = {
        'book':addBooks.objects.get(id = id)
    }  
    return render(request,'pages/bookview.html', context)

######    edit Book   #################
@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['admin'])
def editBook(request):
    context = {
        'books':addBooks.objects.all(),
    }  
    return render(request,'pages/editBook.html',context)

#####   ubdate Book    ##########
@login_required(login_url='loginUser')
@allowed_users(allowed_roles=['admin'])
def update(request, id):
    book_id=addBooks.objects.get(id=id)
    if request.method == 'POST':
        book_save =BookForm(request.POST,request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('editBook')
    else:
        book_save=BookForm(instance=book_id)
    context ={
        'form':book_save,
    }
    return render(request,'pages/update.html', context)

@login_required(login_url='loginAdmin')
@allowed_users(allowed_roles=['admin'])
def addBook(request):
    if request.method== 'POST':
        add_book =BookForm(request.POST)
        if add_book.is_valid():
            add_book.save()

    context={
        'books':addBooks.objects.all(),
        'form': BookForm(),
    }
    return render(request,'pages/addbook.html', context)

def forbidden(request):
    return render(request, 'pages/forbidden.html')

def goHome(request):
    if request.user.groups.filter(name = 'customer'):
        return redirect('homeeUser')
    if request.user.groups.filter(name = 'admin'):
        return redirect('homeeAdmin')
    else:
        return redirect('index')