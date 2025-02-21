from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def changeusername(request):
    if request.method == "POST":
        new_username = request.POST.get("username")
        if new_username:
            request.user.username = new_username
            request.user.save()
            messages.success(request, "Username changed successfully!")
            return redirect("home")
        else:
            messages.error(request, "Please enter a valid username.")

    return render(request, 'users/changeUsername.html')


@login_required
def changeemail(request):
    if request.method == "POST":
        new_email = request.POST.get("email")
        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, "Email changed successfully!")
            return redirect("home")
        else:
            messages.error(request, "Please enter a valid email address.")

    return render(request, 'users/changeEmail.html')
