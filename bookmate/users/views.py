from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш акаунт створено! Тепер ви можете увійти.")
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
