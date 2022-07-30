
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=6)
    description = models.TextField()
    course_head = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})
    
    