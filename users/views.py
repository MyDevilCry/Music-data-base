from django.contrib import auth, messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import CustomUserCreationForm, ProfileForm, UserLoginForm

User = get_user_model()


class UserRegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Ви успішно зареєструвались!")
        return redirect("users:login")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        messages.success(self.request, f" {username} Ви успішно авторизувались!")
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Ви успішно оновили профіль")
        return super().form_valid(form)


def logout(request):
    auth.logout(request)
    messages.success(request, "Ви вийшли з акаунту")
    return redirect("artists:index")
