from django.db import models

class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self. name  


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=50, default='support')  # Add this if missing
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"