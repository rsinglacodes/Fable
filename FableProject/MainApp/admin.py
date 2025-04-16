from django.contrib import admin
from .models import feedback

from .models import ContactMessage

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','email','comment','created_at']

admin.site.register(feedback, FeedbackAdmin)




@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)  # Only created_at should be read-only
    ordering = ('-created_at',)