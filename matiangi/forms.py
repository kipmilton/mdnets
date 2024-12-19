from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('transcriber', 'Transcriber'),
        ('coder', 'Coder'),
        ('graphic_designer', 'Graphic Designer'),
        ('client', 'Client'),
    ]
    
    # Role field is hidden, but it will still be submitted
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user


class GraphicDesignRequestForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email Address')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    service_type = forms.CharField(max_length=100, label='Type of Service (e.g., logo, banner, etc.)')
    description = forms.CharField(widget=forms.Textarea, label='Description of the Request')
    preferred_contact_time = forms.CharField(max_length=50, label='Preferred Contact Time (optional)', required=False)






from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

# # Custom user creation form
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

# Custom authentication form
class CustomAuthenticationForm(AuthenticationForm):
    pass


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('transcriber', 'Transcriber'),
        ('coder', 'Coder'),
        ('graphic_designer', 'Graphic Designer'),
        ('client', 'Client'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']



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