from django.db import models
from django.core.validators import MinValueValidator

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    cta_primary_text = models.CharField(max_length=50)
    cta_secondary_text = models.CharField(max_length=50)
    background_image = models.ImageField(upload_to='hero/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='menu/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    main_content = models.TextField()
    side_content = models.TextField()
    image = models.ImageField(upload_to='about/')
    years_serving = models.IntegerField(default=5)
    happy_customers = models.IntegerField(default=10000)
    coffee_varieties = models.IntegerField(default=15)

    class Meta:
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    weekday_hours = models.CharField(max_length=100)
    weekend_hours = models.CharField(max_length=100)
    map_link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return self.email

class Review(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('fr', 'French'),
        ('ar', 'Arabic'),
    ]
    
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1)])
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    date_posted = models.DateField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} - {self.rating}★"

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.platform
