from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'matiangi'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('accounts/login/', views.login_page, name='login_page'),  # Consider renaming or removing one of these login paths
    path('register/', views.register, name='register'),  # Keep only one path for register
    path('contact/', views.contact, name='contact'),
    path('graphic-design-request/', views.graphic_design_request, name='graphic_design_request'),
    path('transcription-home/', views.transcription_home, name='transcription_home'),
    path('transcription-test/', views.transcription_test, name='transcription_test'),  # You might want to protect this with @login_required
    path('transcription-task/', views.transcription_task, name='transcription_task'),  # Fixed view name
    path('coder/', views.coder_debug, name='coder_debug'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('graphic_desighner_login/', views.graphic_desighner_login, name='graphic_desighner_login'),
    
    # Change 'submit-resume/' to a more appropriate URL for freelancer registration
    path('freelancer/register/', views.freelancer_register, name='freelancer_register'),
    
    # Dashboard paths
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
    path('dashboard/transcriber/', views.transcriber_dashboard, name='transcriber_dashboard'),
    path('dashboard/coder/', views.coder_dashboard, name='coder_dashboard'),
    path('dashboard/designer/', views.designer_dashboard, name='designer_dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    
    # Unauthorized page
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    
    # Client-specific code submission
    path('submit-code/', views.client_submit_code, name='client_submit_code'),

    # Login pages for each role
    path('login/client/', views.client_login, name='client_login'),
    path('login/transcriber/', views.transcriber_login, name='transcriber_login'),
    path('login/coder/', views.coder_login, name='coder_login'),
    path('login/graphic-designer/', views.graphic_designer_login, name='graphic_designer_login'),
    path('login/staff/', views.staff_login, name='staff_login'),

    # Register pages for each role
    path('register/client/', views.client_register, name='client_register'),
    path('register/transcriber/', views.transcriber_register, name='transcriber_register'),
    path('register/coder/', views.coder_register, name='coder_register'),
    path('register/graphic-designer/', views.graphic_designer_register, name='graphic_designer_register'),
    path('register/staff/', views.staff_register, name='staff_register'),
]

# Add static file handling during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






# # from django.urls import path
# # from . import views
# # from django.conf import settings
# # from django.conf.urls.static import static

# # app_name = 'matiangi'

# # urlpatterns = [
# #     path('', views.home_page, name='home_page'),  
# #     path('accounts/login/', views.login_page, name='login_page'),
# #     path('accounts/register/', views.register, name='register'),
# #     path('contact/', views.contact, name='contact'),
# #     path('graphic-design-request/', views.graphic_design_request, name='graphic_design_request'),
# #     path('transcription-home/', views.transcription_home, name='transcription_home'),  
# #     path('transcription-test/', views.transcription_test, name='transcription_test'),
# #     path('transcription-task/', views.TranscriptionTask, name='transcription_task'),
# #     path('coder/', views.coder_debug, name='coder_debug'),
# #     path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
# #     path('transcriber_register/', views.transcriber_register, name='transcriber_register'),
# #     path('transcriber_login/', views.transcriber_login, name='transcriber_login'),
# #     path('submit-resume/', views.submit_resume, name='submit_resume'),
# #     path('register/', views.register, name='register'),
# #     path('login/', views.login_view, name='login'),
# #     path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
# #     path('dashboard/transcriber/', views.transcriber_dashboard, name='transcriber_dashboard'),
# #     path('dashboard/coder/', views.coder_dashboard, name='coder_dashboard'),
# #     path('dashboard/designer/', views.designer_dashboard, name='designer_dashboard'),
# #     path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
# #     path('unauthorized/', views.unauthorized, name='unauthorized'),
# # ]

# # # Add static file handling during development
# # if settings.DEBUG:
# #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# app_name = 'matiangi'

# urlpatterns = [
#     path('', views.home_page, name='home_page'),
#     path('accounts/login/', views.login_page, name='login_page'),  # Consider renaming or removing one of these login paths
#     path('register/', views.register, name='register'),  # Keep only one path for register
#     path('contact/', views.contact, name='contact'),
#     path('graphic-design-request/', views.graphic_design_request, name='graphic_design_request'),
#     path('transcription-home/', views.transcription_home, name='transcription_home'),
#     path('transcription-test/', views.transcription_test, name='transcription_test'),  # You might want to protect this with @login_required
#     path('transcription-task/', views.transcription_task, name='transcription_task'),  # Fixed view name
#     path('coder/', views.coder_debug, name='coder_debug'),
#     path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
#     path('submit-resume/', views.submit_resume, name='submit_resume'),
#     path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),
#     path('dashboard/transcriber/', views.transcriber_dashboard, name='transcriber_dashboard'),
#     path('dashboard/coder/', views.coder_dashboard, name='coder_dashboard'),
#     path('dashboard/designer/', views.designer_dashboard, name='designer_dashboard'),
#     path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
#     path('unauthorized/', views.unauthorized, name='unauthorized'),
#     #path('client_submit_code/', views.client_submit_code, name='client_submit_code')
#     path('submit-code/', views.client_submit_code, name='client_submit_code'),
#     path('submit-resume/', views.freelancer_register, name='freelancer_register'),
#     # Login pages for each role
#     path('login/client/', views.client_login, name='client_login'),
#     path('login/transcriber/', views.transcriber_login, name='transcriber_login'),
#     path('login/coder/', views.coder_login, name='coder_login'),
#     path('login/graphic-designer/', views.graphic_designer_login, name='graphic_designer_login'),
#     path('login/staff/', views.staff_login, name='staff_login'),

#     # Register pages for each role
#     path('register/client/', views.client_register, name='client_register'),
#     path('register/transcriber/', views.transcriber_register, name='transcriber_register'),
#     path('register/coder/', views.coder_register, name='coder_register'),
#     path('register/graphic-designer/', views.graphic_designer_register, name='graphic_designer_register'),
#     path('register/staff/', views.staff_register, name='staff_register'),
# ]

# # Add static file handling during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
