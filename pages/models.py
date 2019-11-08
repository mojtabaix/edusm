from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()


class Course(models.Model):
    department = models.CharField(max_length=150, blank=False)
    name = models.CharField(max_length=150, blank=False)

    course_number = models.IntegerField(blank=False)

    group_number = models.IntegerField(blank=False)

    teacher = models.CharField(max_length=150, blank=False)
    exam_date = models.DateField(blank=False, default="2016-01-11")

    start_time = models.CharField(max_length=7)
    end_time = models.CharField(max_length=6)
    Saturday = 'شنبه'
    Sunday = 'یک شنبه'
    Monday = 'دو شنیه'
    Tuesday = 'سه شنبه'
    Wensday = 'چهارشنیه'
    DAYS = [
        (Saturday, 'شنبه'),
        (Sunday, 'یک شنبه'),
        (Monday, 'دو شنیه'),
        (Tuesday, 'سه شنبه'),
        (Wensday, 'چهارشنیه')
    ]
    first_day = models.CharField(
        max_length=20,
        choices=DAYS,
        blank=False
    )

    second_day = models.CharField(
        max_length=20,
        choices=DAYS,
    )
    # first_day.

