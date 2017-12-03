from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateField(auto_now=True)
    published_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.pk) + '_' + self.title
