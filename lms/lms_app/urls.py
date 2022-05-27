from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns =[     
    path('addBook',views.addBook, name='addBook'),
    path('books',views.books, name='books'),
    path('bookview',views.bookView, name='bookview'),
    path('editBook',views.editBook, name='editBook'),
    path('Home',views.home, name='index'),
    path('homeeAdmin',views.homeeAdmin, name='homeeAdmin'),
    path('homeeUser',views.homeeUser, name='homeeUser'),    
    path('profile',views.profile, name='profile'),
    path('editProfile',views.editProfile, name = 'editProfile'),
    path('signUP',views.signUP, name='signUP'),
    path('registerAdmin',views.registerAdmin, name='registerAdmin'),
    path('registerUser',views.registerUser, name='registerUser'),
    path('loginUser',views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name = 'logoutUser'), 
    path('forbidden', views.forbidden, name = 'forbidden'),    
    path('update /<int:id>/ ',views.update, name='update'),      
    path('', views.goHome, name = 'home'),
    path('<int:id>', views.bookView, name='viewBook')

    # path('SignUp',views.SignUp, name='SignUp'),
    # path('Login',views.Login, name='Login'),
]