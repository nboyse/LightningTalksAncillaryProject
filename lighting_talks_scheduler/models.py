import uuid
from django.db import models
from django.core.validators import RegexValidator


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
