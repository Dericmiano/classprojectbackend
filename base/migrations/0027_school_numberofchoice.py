# Generated by Django 3.2.9 on 2022-01-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_applicationitem_studentscoreaverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='numberOfChoice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
