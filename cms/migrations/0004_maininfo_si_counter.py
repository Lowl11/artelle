# Generated by Django 2.0.13 on 2019-08-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_maininfo_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='maininfo',
            name='si_counter',
            field=models.IntegerField(default=0),
        ),
    ]
