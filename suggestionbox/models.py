from django.db import models
from django.utils import timezone

from django.urls import reverse
# Create your models here.

TYPE_CHOICES = (('feedback','FEEDBACK'),('suggestion','SUGGESTION'))

class Post(models.Model):
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='feedback')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1024)
    name = models.CharField(max_length=100, blank=True)
    submit_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.title    

    def get_absolute_url(self):
        return reverse("thankyou")


    def submit(self):
        self.submit_date = timezone.now()
        self.save()
