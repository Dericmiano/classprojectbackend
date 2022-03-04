# Generated by Django 3.2.9 on 2022-01-19 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_remove_school_numberofchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationitem',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.student'),
        ),
        migrations.AddField(
            model_name='applicationitem',
            name='studentScoreAverage',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=7),
        ),
    ]
