from django import forms
from .models import LightningTalk, Person
from django.forms.widgets import Widget
from datetime import date, datetime



class DateWidget(Widget):
    template_name="lighting_talks_scheduler\templates\widgets\date_field.html"

class UserNameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True


    class Meta:
        model = Person
        fields = (
            "first_name",
            "last_name",
        )

        # def clean(self):
        # cleaned_data = super().clean()


class EmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta:
        model = Person
        fields = ("email", "confirm_your_email_address")

class DateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs),

        date_of_talk = date(

        require_all_fields=False,
        help_text=f"For example, 20 2 {datetime.now().year-2}",
        error_messages={
            "required": "Enter the date of your Lightning Talk",
            "incomplete": "Enter the full date of your Lightning Talk",
            "invalid": "Your Lightning Talk must be booked on a valid date",
            "day": {
                "incomplete": "Booking date must include a day",
                "invalid": "Booking date must be a real date",
            },
            "month": {
                "incomplete": "Booking date must include a month",
                "invalid": "Booking Date must be a real date",
            },
            "year": {
                "incomplete": "Booking date must include a year",
                "invalid": "Booking date must be a real date",
            },
        },
    )


    class Meta:
        model=LightningTalk
        fields=("day", "month", "year",)

        # def clean(self):
        # cleaned_data = super().clean()
