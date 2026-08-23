from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        placeholders={
            'username': 'Enter your username',
            'first_name':'Enter your first name',
            'last_name':'Enter your last name',
            'email': 'Enter your email',
            'password1': 'Password',
            'password2': 'Enter your password again'

        }
        for field_name,placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'placeholder':placeholder})



class UserLoginForm(AuthenticationForm):

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

        username=forms.CharField(
            max_length=20,label="username",
            widget=forms.TextInput(attrs={"class":"Form-control",
                                          "placeholder":"Username"}))

        password=forms.CharField(
            label="password",
            widget=forms.PasswordInput(attrs={"class":"Form-control",
                                          "placeholder":"Password"}))



class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']











