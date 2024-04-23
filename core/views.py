from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class GalleryView(TemplateView):
    template_name = 'gallery.html'
    
class ProductView(TemplateView):
    template_name = 'product.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

