# Generated by Django 2.2.7 on 2019-11-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20191108_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='course',
            name='first_day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یک شنبه', 'یک شنبه'), ('دو شنبه', 'دو شنیه'), ('سه شنبه', 'سه شنبه'), ('چهارشنبه', 'چهارشنیه')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_day',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یک شنبه', 'یک شنبه'), ('دو شنبه', 'دو شنیه'), ('سه شنبه', 'سه شنبه'), ('چهارشنبه', 'چهارشنیه')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_time',
            field=models.CharField(max_length=7),
        ),
    ]
