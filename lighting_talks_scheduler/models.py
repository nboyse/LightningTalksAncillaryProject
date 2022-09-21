from django.db import models
import datetime

class Person(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class LightningTalk(models.Model):
    user= models.ForeignKey(Person, on_delete=models.PROTECT)
    time= models.TimeField()
    date= models.DateField()
    title=models.CharField(max_length=240)
    subject=models.CharField(max_length=240)