
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student,Instructor,Profile


@receiver(post_save,sender=User)
def create_student(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        temp=sender.objects.last().email
        if temp[:4]=='prof':
            print(temp)
            Instructor.objects.create(user=instance)
        else:
            Student.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profle(sender,instance,**kwargs):
    instance.profile.save()
    # temp=instance.email
    # if temp[:4]=='prof':
    #     print(temp)
    #     Instructor.objects.create(user=instance)
    # else:
    #     Student.objects.create(user=instance)
