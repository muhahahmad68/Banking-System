from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account has been created successfully")
            new_user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password1"])
            login(request, new_user)
            return redirect('index')
    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'sign-up.html', context)


def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect('index')
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect('sign-in')

        except :
                messages.warning(request, "User does not exist")
    return render(request, 'sign-in.html')



def LogoutView(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('sign-in')
