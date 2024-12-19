from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, GraphicDesignRequestForm
from .models import TranscriptionTask


# # Create your views here.
def home_page(request):
    context = {}
    return render(request, "index.html", context)


def register(request):
    """Display the gallery page"""
    return render(request, "register.html")

def contact(request):
    """Display the contact page"""
    return render(request, 'contact.html')

# Home page view
def home_page(request):
    return render(request, "index.html")



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']

            # Assign user to the selected group
            group = Group.objects.get(name=role)
            user.groups.add(group)

            # Authenticate and log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a common home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a common dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


from django.contrib.auth.decorators import login_required, user_passes_test

# Check if user belongs to a specific group
def group_required(group_name):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            return redirect('unauthorized')  # Redirect unauthorized users
        return _wrapped_view
    return decorator

# Staff Dashboard
@group_required('staff')
def staff_dashboard(request):
    return render(request, 'dashboards/staff_dashboard.html')

# Transcriber Dashboard
@group_required('transcriber')
def transcriber_dashboard(request):
    return render(request, 'dashboards/transcriber_dashboard.html')

# Coder Dashboard
@group_required('coder')
def coder_dashboard(request):
    return render(request, 'dashboards/coder_dashboard.html')

# Graphic Designer Dashboard
@group_required('graphic_designer')
def designer_dashboard(request):
    return render(request, 'dashboards/designer_dashboard.html')

# Client Dashboard
@group_required('client')
def client_dashboard(request):
    return render(request, 'dashboards/client_dashboard.html')





#Login page view
def login_page(request):
    return render(request, "login.html")


# # Register View
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('transcription_home.html')  # Redirect to the transcription page
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'transcriber_register.html', {'form': form})


# # Register page view
# def transcriber_register(request):
#     """Display the register page and handle registration"""
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('transcription_home.html')  # Redirect to the transcription home page
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'transcriber_register.html', {'form': form})

# Login view
def transcriber_login(request):
    """Handle user login"""
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('transcription_home.html')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'transcriber_login.html', {'form': form})

# Transcription Test view (Only available for registered users)
@login_required
def transcription_test(request):
    """Display the transcription test page"""
    if request.method == 'POST':
        # Handle the test submission (e.g., storing transcription task)
        task = TranscriptionTask(user=request.user, task_status='pending', earnings=0)
        task.save()
        return redirect('view_task', task_id=task.id)  # Redirect to view task after submitting
    return render(request, 'transcription_test.html')

# View user's transcription tasks and earnings
@login_required
def user_dashboard(request):
    tasks = TranscriptionTask.objects.filter(user=request.user)
    total_earnings = sum(task.earnings for task in tasks)
    return render(request, 'user_dashboard.html', {'tasks': tasks, 'total_earnings': total_earnings})

# Graphic Design Request form view
def graphic_design_request(request):
    """Handle graphic design service request form"""
    if request.method == 'POST':
        form = GraphicDesignRequestForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            service_type = form.cleaned_data['service_type']
            description = form.cleaned_data['description']
            preferred_contact_time = form.cleaned_data['preferred_contact_time']

            # Send an email to the admin (you can replace this with your own logic)
            subject = f"Graphic Design Request from {name}"
            message = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nService Type: {service_type}\nDescription: {description}\nPreferred Contact Time: {preferred_contact_time}"
            send_mail(subject, message, email, ['kipmilton71@gmail.com'], fail_silently=False)

            messages.success(request, "Your graphic design request has been submitted successfully. We'll get back to you shortly.")
            return redirect('matiangi:graphic_design_request')  # Redirect back to the form page after submission
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = GraphicDesignRequestForm()

    return render(request, 'accounts/graphic_design_request.html', {'form': form})

# Transcription Home view
def transcription_home(request):
    return render(request, 'transcription_home.html')

def client_submit_code(request):
    return render(request, 'client_submit_code.html')

# Coder Debug view (handles uploaded code and pasted code)
@csrf_exempt
@login_required  # For simplicity; use CSRF protection in production
def coder_debug(request):
    if request.method == 'POST':
        code_file = request.FILES.get('code_file')
        code_text = request.POST.get('code_text')

        if code_file:
            # Handle uploaded file
            handle_uploaded_file(code_file)
            return HttpResponse("File uploaded successfully.")

        elif code_text:
            # Handle pasted code
            return HttpResponse("Code received successfully.")

        return HttpResponse("No code submitted.")

    return render(request, 'coder.html')

# Submit Resume view (handles resume upload)
@csrf_exempt  # For simplicity; use CSRF protection in production
def submit_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        message = request.POST.get('message')

        if resume_file:
            # Handle resume upload
            handle_uploaded_file(resume_file)
            return HttpResponse("Resume uploaded successfully.")

        return HttpResponse("No resume submitted.")

    return redirect('transcription_home')

# Helper function to handle uploaded files
def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def client_submit_code(request):
    if request.method == 'POST':
        # Handle code submission here
        # Code for saving the file or text will go here
        code_file = request.FILES.get('code_file')
        code_text = request.POST.get('code_text')

        if code_file or code_text:
            # Process the file or text, e.g., save it, send for debugging, etc.
            messages.success(request, 'Your code has been submitted for debugging!')
            return redirect('matiangi:home_page')  # Redirect to the homepage or appropriate page
        else:
            messages.error(request, 'Please upload a file or paste code to proceed.')

    return render(request, 'client_submit_code.html')

# View for freelancers to submit resume
def freelancer_register(request):
    if request.method == 'POST':
        # Handle resume submission here
        resume_file = request.FILES.get('resume_file')
        message = request.POST.get('message')

        if resume_file and message:
            # Process the resume file and message, e.g., save it, notify the team, etc.
            messages.success(request, 'Your resume has been submitted!')
            return redirect('matiangi:home_page')  # Redirect to the homepage or appropriate page
        else:
            messages.error(request, 'Please upload your resume and provide a message.')

    return render(request, 'freelancer_register.html')

















# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import TranscriptionTask

# Register View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('transcription_home')  # Redirect to the transcription page
    else:
        form = CustomUserCreationForm()
    return render(request, 'transcriber_register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('transcription_home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'transcriber_login.html', {'form': form})

# Transcription Test View (Only available for registered users)
@login_required
def transcription_test(request):
    if request.method == 'POST':
        # Handle the test submission (e.g., storing transcription task)
        task = TranscriptionTask(user=request.user, task_status='pending', earnings=0)
        task.save()
        return redirect('view_task', task_id=task.id)  # Redirect to view task after submitting
    return render(request, 'transcription_test.html')

# View user's transcription tasks and earnings
@login_required
def user_dashboard(request):
    tasks = TranscriptionTask.objects.filter(user=request.user)
    total_earnings = sum(task.earnings for task in tasks)
    return render(request, 'user_dashboard.html', {'tasks': tasks, 'total_earnings': total_earnings})



def graphic_design_request(request):
    """Handle graphic design service request form"""
    if request.method == 'POST':
        form = GraphicDesignRequestForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            service_type = form.cleaned_data['service_type']
            description = form.cleaned_data['description']
            preferred_contact_time = form.cleaned_data['preferred_contact_time']

            # You can save this data to the database or send it via email
            # For this example, let's send an email to the admin

            subject = f"Graphic Design Request from {name}"
            message = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nService Type: {service_type}\nDescription: {description}\nPreferred Contact Time: {preferred_contact_time}"
            send_mail(
                subject,
                message,
                email,  # Sender email
                ['admin@example.com'],  # Admin email (replace with actual admin email)
                fail_silently=False,
            )

            messages.success(request, "Your graphic design request has been submitted successfully. We'll get back to you shortly.")
            return redirect('thee_app:graphic_design_request')  # Redirect back to the form page after submission
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = GraphicDesignRequestForm()

    return render(request, 'accounts/graphic_design_request.html', {'form': form})


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def transcription_home(request):
    return render(request, 'transcription_home.html')

def transcription_test(request):
    return render(request, 'transcription_test.html')

@login_required
def transcription_task(request):
    return render(request, 'transcription_task.html')

def unauthorized(request):
    return render(request, 'unauthorized.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

def client_login(request):
    """Handle client login"""
    return handle_login(request, 'client_login.html')

def transcriber_login(request):
    """Handle transcriber login"""
    return handle_login(request, 'transcriber_login.html')

def coder_login(request):
    """Handle coder login"""
    return handle_login(request, 'coder_login.html')

def graphic_designer_login(request):
    """Handle graphic designer login"""
    return handle_login(request, 'graphic_designer_login.html')

def staff_login(request):
    """Handle staff login"""
    return handle_login(request, 'staff_login.html')

# Helper function to handle login for different user roles
def handle_login(request, template_name):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('matiangi:user_dashboard')  # Redirect to the user dashboard or home
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = CustomAuthenticationForm()
    return render(request, template_name, {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm

# Register views for each role
def client_register(request):
    return handle_register(request, 'client_register.html', 'client')

def transcriber_register(request):
    return handle_register(request, 'transcriber_register.html', 'transcriber')

def coder_register(request):
    return handle_register(request, 'coder_register.html', 'coder')

def graphic_designer_register(request):
    return handle_register(request, 'graphic_designer_register.html', 'graphic_designer')

def staff_register(request):
    return handle_register(request, 'staff_register.html', 'staff')

# Helper function to handle registration for different user roles
def handle_register(request, template_name, role):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can also save role into the user profile model or handle it as needed
            user_role = form.cleaned_data['role']  # This can be used for further handling
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('matiangi:user_dashboard')  # Redirect to user dashboard or home
            else:
                messages.error(request, "Login failed.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = CustomUserCreationForm(initial={'role': role})
    return render(request, template_name, {'form': form})





@login_required
def some_restricted_view(request):
    if not request.user.has_permission('some_permission'):
        return redirect('matiangi:unauthorized')
    return render(request, 'some_restricted_template.html')


@csrf_exempt  # For simplicity; use CSRF protection in production
def coder_debug(request):
    if request.method == 'POST':
        code_file = request.FILES.get('code_file')
        code_text = request.POST.get('code_text')

        if code_file:
            # Handle uploaded file
            handle_uploaded_file(code_file)
            return HttpResponse("File uploaded successfully.")

        elif code_text:
            # Handle pasted code
            return HttpResponse("Code received successfully.")

        return HttpResponse("No code submitted.")

    return render(request, 'coder.html')

@csrf_exempt  # For simplicity; use CSRF protection in production
def submit_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        message = request.POST.get('message')

        if resume_file:
            # Handle resume upload
            handle_uploaded_file(resume_file)
            return HttpResponse("Resume uploaded successfully.")

        return HttpResponse("No resume submitted.")

    return redirect('transcription_home')

# def handle_uploaded_file(f):
#     with open(f'uploads/{f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


# def login_page(request):
#     """Login view"""
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, "You are now logged in!")
#             return redirect('thee_app:home')  # Redirect to the homepage or dashboard
#         else:
#             messages.error(request, "Invalid login credentials.")
    
#     return render(request, 'accounts/login.html')




# def register(request):
#     """Registration view"""
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:
#             try:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save()
#                 messages.success(request, "Account created successfully.")
#                 return redirect('thee_app:login_page')  # Redirect to the login page after successful registration
#             except Exception as e:
#                 messages.error(request, f"Error: {str(e)}")
#         else:
#             messages.error(request, "Passwords do not match.")
    
#     return render(request, 'accounts/register.html')
         