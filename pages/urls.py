from django.conf.urls import url, include
from .views import about_view, terms_view, pay_view

urlpatterns = [
    url('about/', about_view, name="about"),
    url('terms-conditions/', terms_view, name="terms"),
    url('payments/', pay_view, name="payments")

]