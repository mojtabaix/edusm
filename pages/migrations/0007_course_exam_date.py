# Generated by Django 2.2.7 on 2019-11-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20191108_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exam_date',
            field=models.DateField(default='2016-01-11'),
        ),
    ]