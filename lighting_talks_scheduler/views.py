from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseServerError
from django.core.validators import ValidationError
from .models import Person
from .forms import DateForm, UserNameForm
from .forms import EmailForm


def homepage(request):
    return render(request, "homepage.html")


def name(request):
    return render(request, "name.html")


def email(request):
    return render(request, "email.html")


class NameView(CreateView):
    form_class = UserNameForm
    template_name = "name.html"
    success_url = "email"

    def form_valid(self, form):
        try:
            Person.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            return redirect(reverse("email"))
        except Exception:
            return HttpResponseServerError(
                "error creating person object"
            )


class EmailView(CreateView):
    model = Person
    template_name = "email.html"
    form_class = EmailForm
    # todo - you need to create this the same way I created the NameForm
    # form_class = EmailForm

    def form_valid(self, form):
        try:
            Person.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
        )
            return redirect(reverse("email"))
        except ValidationError as e:
            return HttpResponseServerError(
                f"error creating person object {e.messages}"
        )


class DateView(CreateView):
    model = Person
    template_name = "date.html"
    form_class = DateForm
    # todo - you need to create this the same way I created the NameForm
    # form_class = EmailForm

    def form_valid(self, form):
        try:
            Person.objects.create(
                day=form.cleaned_data["day"],
                month=form.cleaned_data["month"],
                year=form.cleaned_data["year"],
        )
            return redirect(reverse("email"))
        except ValidationError as e:
            return HttpResponseServerError(
                f"error creating person object {e.messages}"
        )