# Generated by Django 2.2.7 on 2019-11-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_course_exam_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='my_courses',
            field=models.ManyToManyField(to='pages.Course'),
        ),
    ]