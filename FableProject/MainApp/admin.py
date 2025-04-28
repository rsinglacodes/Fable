from django.contrib import admin
from .models import feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','email','comment','suggestion','created_at']

admin.site.register(feedback, FeedbackAdmin)



