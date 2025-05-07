from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment', 'suggestion', 'sentiment', 'mood', 'created_at']

admin.site.register(Feedback, FeedbackAdmin)