# Generated by Django 2.2.7 on 2019-11-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('course_number', models.IntegerField()),
                ('group_number', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=150)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('first_day', models.CharField(max_length=150)),
                ('second_day', models.CharField(max_length=150)),
            ],
        ),
    ]
