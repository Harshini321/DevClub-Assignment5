from django.db import models
# all models inherit from this models class
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
# Create your models here.


class Document(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='lecture_notes')
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('document-detail',kwargs={'pk':self.pk})