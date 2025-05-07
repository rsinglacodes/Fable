from django.db import models
from django.utils.text import slugify
from django.conf import settings
from AuthApp.models import AppUser

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
    # Add slug field - make it nullable initially
    slug = models.SlugField(unique=True, max_length=50, null=True, blank=True)
    
    # Image URLs
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)
    image5_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.hotel_name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.hotel_name)
            slug = base_slug
            counter = 1
            # Check if the slug exists and generate a unique one if needed
            while Hotel.objects.filter(slug=slug).exclude(hotel_name=self.hotel_name).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)



class Booking(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Add this line
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    total_price = models.FloatField(default=0.0)  # Add this field to store the calculated price
    
    def __str__(self):
        return f"{self.user.email} - {self.hotel_name.hotel_name} ({self.check_in} to {self.check_out})"
    
    def calculate_total_price(self):
        nights = (self.check_out - self.check_in).days
        return self.hotel_name.price * nights