from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'matiangi'

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Home page
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('graphic-design-request/', views.graphic_design_request, name='graphic_design_request'),
    path('transcription-home/', views.transcription_home, name='transcription_home'),  # Corrected to avoid conflict
    path('transcription-test/', views.transcription_test, name='transcription_test'),
    path('transcription-task/', views.TranscriptionTask, name='transcription_task'),
    path('coder/', views.coder_debug, name='coder_debug'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('transcriber_register/', views.register, name='transcriber_register'),
    path('transcriber_login/', views.login_view, name='transcriber_login'),
    path('submit-resume/', views.submit_resume, name='submit_resume'),
]

# Add static file handling during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
