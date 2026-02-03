from django.views import View
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm


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
