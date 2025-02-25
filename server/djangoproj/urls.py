from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Authentication and static pages
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    
    # Dynamic React routes:
    path('dealers/', TemplateView.as_view(template_name="index.html")),  # Dealers list
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),  # Dealer details
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),  # Post review page
    
    # Admin and Django app API endpoints
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    
    # Home page route
    path('', TemplateView.as_view(template_name="Home.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
