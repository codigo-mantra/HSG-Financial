from django.views import View
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm

from django.views.generic import ListView, DetailView
from taggit.models import Tag
from .models import Blog, Category
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

class ContactUsView(View):
    template_name = "website/contact_us.html"

    def get(self, request):
        form = ContactUsForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ContactUsForm(request.POST)

        if form.is_valid():
            context = {
                "first_name": form.cleaned_data.get("first_name"),
                "last_name": form.cleaned_data.get("last_name"),
                "phone_number":form.cleaned_data.get("phone_number"),
                "email_address": form.cleaned_data.get("email_address"),
                "message": form.cleaned_data.get("message")
            }
            form.save()
            messages.success(
                    request, "Your query has been submitted successfully."
                )

            html_content = render_to_string(
                "website/emailtemplate.html",
                context
            )
            try:
                send_mail(
                    subject="New Contact Form Submission - HSG Financial",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    message="You have received a new contact form submission.",
                    recipient_list=[settings.EMAIL_HOST_USER],
                    html_message=html_content,  
                    fail_silently=False,
                )

            except Exception as e:
                print("error sending the mail ", str(e))
                
        return render(request, self.template_name, {"form": form})


class AboutUsView(View):
    def get(self, request):
        return render(request, "website/about_us.html")


class IndexView(View):
    def get(self, request):
        return render(request, "website/new_index.html")


class ServicesView(View):
    def get(self, request):
        return render(request, "website/service_detail.html")

class LoanCalculatorView(View):
    def get(self, request):
        return render(request, "website/Calculator.html")

class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, "website/privacy_policy.html")

class SpecificCalculatorView(View):
    def get(self, request):
        return render(request, "website/specific_calculator.html")


class BlogPageView(ListView):
    model = Blog
    template_name = "website/blog.html"
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return (
            Blog.objects
            .filter(is_published=True)
            .select_related('category')
            .prefetch_related('tags')
        )

from django.db.models import Q
from django.views.generic import DetailView
from .models import Blog


class BlogDetailView(DetailView):
    model = Blog
    template_name = "website/blog_detail.html"
    context_object_name = "blog"

    def get_queryset(self):
        return (
            Blog.objects
            .filter(is_published=True)
            .select_related("category", "author")
            .prefetch_related("tags")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.object

        # related by category OR tags
        related_blogs = (
            Blog.objects.filter(is_published=True)
            .filter(
                Q(category=blog.category) |
                Q(tags__in=blog.tags.all())
            )
            .exclude(id=blog.id)
            .distinct()
            .select_related("category", "author")
            .prefetch_related("tags")[:3]
        )

        context["related_blogs"] = related_blogs
        return context
