from django.db import models
from django.contrib.auth.models import User
from users.models import Course
from django.urls import reverse

# Create your models here.
class Grade(models.Model):
    course = models.CharField(max_length=6,default='AAAXXX')
    marks = models.fields.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} {self.course} Grade'
    def get_absolute_url(self):
        return reverse("grade-detail", kwargs={"pk": self.pk})