from django import forms
from .models import ContactUsQuery
import re


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsQuery
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email_address",
            "message",
        ]
        error_messages = {
            "first_name": {
                "required": "First name is required.",
            },
            "last_name": {
                "required": "Last name is required.",
            },
            "phone_number": {
                "required": "Phone number is required.",
            },
            "email_address": {
                "required": "Email address is required.",
                "invalid": "Enter a valid email address.",
            },
            "message": {
                "required": "Message is required.",
            },
        }

    # 🔹 First Name: letters only
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name and not re.match(r'^[A-Za-z]+$', first_name):
            raise forms.ValidationError(
                "First name must contain only letters."
            )

        return first_name

    # 🔹 Last Name: letters only
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")

        if last_name and not re.match(r'^[A-Za-z]+$', last_name):
            raise forms.ValidationError(
                "Last name must contain only letters."
            )

        return last_name

    # 🔹 Phone Number: digits only + length
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")

        if phone:
            if not phone.isdigit():
                raise forms.ValidationError(
                    "Phone number must contain only numbers."
                )

            if len(phone) != 10:
                raise forms.ValidationError(
                    "Phone number must be exactly 10 digits."
                )

        return phone
