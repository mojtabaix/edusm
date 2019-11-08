# Generated by Django 2.2.7 on 2019-11-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20191108_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='teacher_name',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='course',
            name='first_day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یک شنبه', 'یک شنبه'), ('دو شنیه', 'دو شنیه'), ('سه شنبه', 'سه شنبه'), ('چهارشنیه', 'چهارشنیه')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یک شنبه', 'یک شنبه'), ('دو شنیه', 'دو شنیه'), ('سه شنبه', 'سه شنبه'), ('چهارشنیه', 'چهارشنیه')], max_length=20),
        ),
    ]