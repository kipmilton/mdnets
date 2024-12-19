from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group

def create_user_groups():
    roles = ['staff', 'transcriber', 'coder', 'graphic_designer', 'client']
    for role in roles:
        Group.objects.get_or_create(name=role)
