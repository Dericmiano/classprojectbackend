# Generated by Django 3.2.9 on 2022-01-18 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_school_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='numberOfChoice',
        ),
    ]
