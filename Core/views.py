from django.views.generic import TemplateView
from .models import HeroSection, MenuItem, AboutSection, ContactInfo, Review, SocialLink

class HomeView(TemplateView):
    template_name = 'corner_coffeeshop.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'hero': HeroSection.objects.first(),
            'menu_items': MenuItem.objects.filter(is_active=True),
            'about': AboutSection.objects.first(),
            'contact': ContactInfo.objects.first(),
            'featured_reviews': Review.objects.filter(is_featured=True),
            'social_links': SocialLink.objects.filter(is_active=True),
        })
        return context
