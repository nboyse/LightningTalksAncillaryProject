from django import forms
from .models import Person


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
    #     cleaned_data = super().clean()
