from django.views import View
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm

from django.views.generic import ListView, DetailView
from taggit.models import Tag
from .models import Blog, Category


class ContactUsView(View):
    template_name = "website/contact_us.html"

    def get(self, request):
        form = ContactUsForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Your query has been submitted successfully."
            )
            form = ContactUsForm()

        return render(request, self.template_name, {"form": form})


class AboutUsView(View):
    def get(self, request):
        return render(request, "website/about_us.html")


class IndexView(View):
    def get(self, request):
        return render(request, "website/index.html")


class ServicesView(View):
    def get(self, request):
        return render(request, "website/service_detail.html")

class LoanCalculatorView(View):
    def get(self, request):
        return render(request, "website/Calculator.html")


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
