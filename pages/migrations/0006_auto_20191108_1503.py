# Generated by Django 2.2.7 on 2019-11-08 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20191108_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
    ]
