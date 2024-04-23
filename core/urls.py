from django.urls import path
from .views import homeview, ContactView, AboutView, GalleryView, ProductView, ServiceView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('gallery/', GalleryView.as_view(), name="gallery_page"),
    path('product/', ProductView.as_view(), name="product_page"),
    path('service/', ServiceView.as_view(), name="service_page")
]