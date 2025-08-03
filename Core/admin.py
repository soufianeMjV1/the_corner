from django.contrib import admin
from .models import HeroSection, MenuItem, AboutSection, ContactInfo, Review, SocialLink

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'years_serving', 'happy_customers', 'coffee_varieties')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_primary', 'weekday_hours')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'language', 'date_posted', 'is_featured')
    list_filter = ('rating', 'language', 'is_featured')
    search_fields = ('author', 'content')

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'is_active')
    list_filter = ('platform', 'is_active')
