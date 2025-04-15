from django.db import models

class Hotel(models.Model):
    CATEGORIES = [
        ('amazing', 'Amazing'),
        ('beach', 'Beach'),
        ('luxury', 'Luxury'),
        ('countryside', 'Countryside'),
        ('spa', 'Spa and Wellness'),
        ('all', 'All Inclusive'),
        ('amazing-views', 'Amazing Views'),
        ('boutique', 'Boutique'),
        ('lakefront', 'Lakefront'),
        ('beachfront', 'Beachfront'),
        ('design', 'Design'),
        ('golf', 'Golf'),
    ]
    
    hotel_name = models.CharField(primary_key=True, max_length=20, unique=True)
    location = models.CharField(max_length=50)
    price = models.FloatField()
    guests = models.IntegerField()
    category = models.CharField(
        max_length=20, 
        choices=CATEGORIES, 
        default='amazing'  
    )
    
    # Image URLs instead of ImageField
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)
    image5_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.hotel_name}"