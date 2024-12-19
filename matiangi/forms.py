from django import forms

class GraphicDesignRequestForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email Address')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    service_type = forms.CharField(max_length=100, label='Type of Service (e.g., logo, banner, etc.)')
    description = forms.CharField(widget=forms.Textarea, label='Description of the Request')
    preferred_contact_time = forms.CharField(max_length=50, label='Preferred Contact Time (optional)', required=False)


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# class CustomUserCreationForm(UserCreationForm):
#     role_choices = [
#         ('transcriber', 'transcriber'),
#         ('coder', 'coder')
#         ('client', 'transcription Client'),
#         ('normal_user', 'Normal User'),
#     ]
#     role = forms.ChoiceField(choices=role_choices, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'role']     