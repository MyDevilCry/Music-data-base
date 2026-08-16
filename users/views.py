from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from users.forms import CustomUserCreationForm, UserLoginForm


class UserRegistrationView(CreateView):
    template_name='users/registration.html'
    form_class=CustomUserCreationForm
    model=User

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('artists:main')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']= "Реєстрація"
        return context

class UserLoginView(LoginView):
    form_class=UserLoginForm
    template_name='users/login.html'
    extra_context = {"title":"Авторизація"}


class UserProfileView(UpdateView):
    template_name='users/profile.html'







