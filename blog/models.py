from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateField(auto_now=True)
    published_date = models.DateField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

# class User(models.Model):
#     login = models.CharField(max_length='20')
#     email = models.EmailField
#     password = models.CharField()
#     gender_choice = (('male', 'Male'), ('female', 'Female'))
#     gender = models.CharField(choices=gender_choice)


