from django import forms
from .models import LightningTalk, Person
from django.forms.widgets import Widget

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
        super().__init__(*args, **kwargs)
        self.fields["date"].required= True
        self.fields["date"].errors= {
            "required": "Enter a date"
        }
        self.fiel
    class Meta:
        model=LightningTalk
        fields=("day", "month", "year",)

        # def clean(self):
        # cleaned_data = super().clean()
