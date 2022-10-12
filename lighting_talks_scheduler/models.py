import uuid
from django.db import models
import datetime
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm


class Person(models.Model):
    first_name = models.CharField(
        max_length=100, validators=[RegexValidator(regex=r"[a-z]+$")], blank=False
    )
    last_name = models.CharField(
        max_length=100, validators=[RegexValidator(regex=r"[a-z]+$")], blank=False
    )
    email = models.EmailField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class LightningTalk(models.Model):
    user = models.ForeignKey(Person, on_delete=models.PROTECT)
    time = models.TimeField()
    date = models.DateField()
    title = models.CharField(max_length=240)
    subject = models.CharField(max_length=240)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=240)
    last_name = forms.CharField(max_length=240)
    error_messages = {
            NON_FIELD_ERRORS: {
                'empty field': "%(model_name)s's %(field_labels)s are empty",
            }
        }