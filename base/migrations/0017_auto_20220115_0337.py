# Generated by Django 3.2.9 on 2022-01-15 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20211220_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='cutoff',
        ),
        migrations.RemoveField(
            model_name='application',
            name='gender',
        ),
    ]