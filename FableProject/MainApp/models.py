from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField(default="")
    suggestion = models.TextField(default="")
    sentiment = models.CharField(max_length=10, blank=True, null=True)  # Store sentiment (positive/negative/neutral)
    mood = models.CharField(max_length=20, blank=True, null=True)  # New field for mood
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name