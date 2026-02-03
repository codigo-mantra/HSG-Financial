from django.urls import path
from .views import ContactUsView, AboutUsView

urlpatterns = [
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),

]
