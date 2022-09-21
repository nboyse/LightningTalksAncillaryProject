from django.db import models
import datetime

class Person(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class Lightning(models.Model):
    user= models.ForeignKey(Person, on_delete=models.CASCADE)
    time= models.TimeField()
    date= models.DateField()
    title=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)