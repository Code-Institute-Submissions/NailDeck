from django.conf.urls import url, include
from .views import about_view, terms_view, contact_view, social_view, thanks

urlpatterns = [
    url('about/', about_view, name="about"),
    url('terms/', terms_view, name="terms"),
    url('contact/', contact_view, name="contact"),
    url('contact/sent', thanks, name="thanks"),
    url('social/', social_view, name="social"),
]