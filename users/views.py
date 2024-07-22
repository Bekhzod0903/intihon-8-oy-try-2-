from django.contrib.auth import login,logout
from django.shortcuts import render
from django.views import  View
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
# Create your views here.

class RegisterView(View):
    def get(self, request):
        create_form = CustomUserForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'register.html', context=context)

        # username = request.POST['username']
        # email = request.POST['email']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # password = request.POST['password']
        #
        # user = CustomUser.objects.create_user(
        #     username=username,
        #     email=email,
        #     first_name=first_name,
        #     last_name=last_name,
        # )
        # user.set_password(password)
        # user.save()

class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            context = {
                'form': login_form
            }
            return render(request, 'login.html', context=context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')



class LogoutViews(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('register')