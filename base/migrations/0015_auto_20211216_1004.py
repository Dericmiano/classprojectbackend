# Generated by Django 3.2.9 on 2021-12-16 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_school_numberofchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.student'),
        ),
        migrations.AddField(
            model_name='studentscores',
            name='application',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.application'),
        ),
    ]
