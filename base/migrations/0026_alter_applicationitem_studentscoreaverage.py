# Generated by Django 3.2.9 on 2022-01-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_remove_applicationitem_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationitem',
            name='studentScoreAverage',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]