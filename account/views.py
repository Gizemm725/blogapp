from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

def login_request(request):
   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, "account/login.html", {"error": "Kullanıcı adı ve parola zorunludur"})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error": "Kullanıcı adı veya parola yanlış"})
    
    return render(request, "account/login.html")

def register_request(request):
   
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")

        if not all([username, firstname, lastname, email, password, repassword]):
            return render(request, "account/register.html", {"error": "Tüm alanlar zorunludur"})

        if password != repassword:
            return render(request, "account/register.html", {"error": "Parolalar eşleşmiyor"})

        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", {"error": "Bu kullanıcı adı zaten kullanılıyor"})

        if User.objects.filter(email=email).exists():
            return render(request, "account/register.html", {"error": "Bu email zaten kullanılıyor"})

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=firstname,
            last_name=lastname,
            password=password
        )
        user.save()
        return redirect("login")
    
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")