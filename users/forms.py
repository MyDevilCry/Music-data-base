from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','firstname','lastname'],

class UserLoginForm(AuthenticationForm):
        username=forms.CharField(
            max_length=20,label="Логін",
            widget=forms.TextInput(attrs={"class":"Form-control",
                                          "placeholder":"Введіть ім'я користувача"}))
        password=forms.CharField(
            label="Пароль",
            widget=forms.TextInput(attrs={"class":"Form-control",
                                          "placeholder":"Введіть пароль"}))
class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','firstname','lastname','email']











