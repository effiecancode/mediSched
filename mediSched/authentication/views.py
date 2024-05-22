from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, 'Account Created Successfully', extra_tags="success")
            return redirect('authentication:login')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})
