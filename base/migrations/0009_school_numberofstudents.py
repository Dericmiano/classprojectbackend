# Generated by Django 3.2.9 on 2021-12-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='numberOfstudents',
            field=models.IntegerField(blank=True, max_length=7, null=True),
        ),
    ]
