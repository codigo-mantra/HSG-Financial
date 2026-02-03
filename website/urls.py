from django.urls import path
from .views import ContactUsView, AboutUsView, IndexView, BlogPageView, BlogDetailView,LoanCalculatorView,ServicesView

urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("contact-us/", ContactUsView.as_view(), name="contact_us"),
    path("about-us/", AboutUsView.as_view(), name="about_us"),
    path("loan-calculator/", LoanCalculatorView.as_view(), name="loan_calculator"),
    path("blog/", BlogPageView.as_view(), name="blogs_page"),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path("service-details/", ServicesView.as_view(), name="service_detail_page"),





    

]
