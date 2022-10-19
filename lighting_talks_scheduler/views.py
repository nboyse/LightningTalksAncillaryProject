from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from .models import Person
from .forms import UserNameForm
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
    success_url= 'email'
    # todo - create this view
    # success_url = 'email'

    def form_valid(self, form):
        return Person.objects.create(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )


class EmailView(CreateView):
    model = Person
    template_name = "email.html"
    form_class= EmailForm
    # todo - you need to create this the same way I created the NameForm
    # form_class = EmailForm

    def form_valid(self, form):
        Person.objects.create(
            email=form.cleaned_data["email"],
            confirm_your_email_address=form.cleaned_data["confirm_your_email_address"]
        )

        # todo - redirect this (set up urls.py, views etc. for the next trello ticket after you've done the email one)
        # return redirect(reverse("next_trello_ticket"))
        return redirect(reverse("next_trello_ticket"))
