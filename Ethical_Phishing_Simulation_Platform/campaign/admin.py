from django.contrib import admin

# Register your models here.
from .models import TargetUser, EmailEvent  # import your models

admin.site.register(TargetUser)
admin.site.register(EmailEvent)
