# Generated by Django 3.2.9 on 2021-11-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_application_applicationitem_studentscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]