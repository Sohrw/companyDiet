from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import datetime as dt 
from .models import Profile

User = get_user_model()

def login_view(request):
    
    if request.method == "POST":
        username=request.POST["username"]
        password = request.POST["password"] 
        user= authenticate(username=username, password=password)
        if user is not None:
            print("GOOD")
            login(request, user)
            
        else:
            print("not good")        
    
    return render(request, "user/login.html")


def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        
        
        hashed_password = make_password(password)  # 비밀번호 암호화
        
        user = User.objects.create(username=username, password=hashed_password, email=email)
        user.firstname = firstname
        user.lastname = lastname

        user.save()
        return redirect("user:login")
    return render(request, "user/signup.html")

from .forms import SaladForm

def salad_decision(request):
    Users_is_salad = User.objects.values_list('is_salad')
    Users_username = User.objects.values_list('username')
    Users_choice_date = User.objects.values_list('choice_date')
    users = User.objects.all()
    now = dt.datetime.now()
    only_date = now.date()
    if request.method == 'POST':
        salad_choice = request.POST.get('salad_choice')
        
    
        print(Users_is_salad)
        print(Users_username)
        print(Users_choice_date)
        print(only_date)
        
    
        # print(now)
        if salad_choice == 'yes':
            if request.user.is_authenticated:
                user = User.objects.get(pk=request.user.pk)
                user.is_salad = True
                user.save()
                Users = User.objects.all()
                # user.choice_date = now
                print(Users_is_salad)
                print(Users_username)
                print(User.objects.all())
                
            return redirect("user:decision")
        elif salad_choice == 'no':
            if request.user.is_authenticated:
                user = User.objects.get(pk=request.user.pk)
                user.is_salad = False
                # user.choice_date = now
                user.save()
                
                
                print(Users_is_salad)
                print(Users_username)
                print(User.objects.all())
            return redirect("user:decision")
    return render(request, 'user/decision.html',{'users': users, 'now':only_date})

def profile(request):
    
    profile=Profile.objects.last()
    print(Profile.objects.values_list('upload_date'))
    return render(request,'user/diet.html',{'profile':profile})

def upload(request):
    return render(request, 'user/editdiet.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    try:
        form.image=request.FILES['image']
    except: 
        pass
    Profile.objects.all().delete()
    form.save()
    return redirect('user:diet')   