from django.db import models

class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    
    comment = models.TextField(default="")
    
    created_at = models.DateTimeField(auto_now_add=True)



    def _str_(self):
        return self. name   


 # MainApp/models.py

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()  # Remove unique=True
    message = models.TextField()  # Remove unique=True
    created_at = models.DateTimeField(auto_now_add=True)


    def str(self):
        return f"{self.name} - {self.email}"