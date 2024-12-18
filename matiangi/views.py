from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def home_page(request):
    context = {}
    return render(request, "index.html", context)

def login_page(request):
    """Display the appointment page"""
    return render(request, "login.html")

def register(request):
    """Display the gallery page"""
    return render(request, "register.html")

def contact(request):
    """Display the contact page"""
    return render(request, 'contact.html')

def login_page(request):
    """Login view"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('thee_app:home')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, "Invalid login credentials")
    
    return render(request, 'accounts/login.html')


def register(request):
    """Registration view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Account created successfully.")
                return redirect('thee_app:login_page')  # Redirect to the login page after successful registration
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'accounts/register.html')
