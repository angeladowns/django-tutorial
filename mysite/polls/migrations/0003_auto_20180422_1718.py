# Generated by Django 2.0.4 on 2018-04-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Add a bio please', max_length=75),
        ),
        migrations.AddField(
            model_name='profile',
            name='recently_active',
            field=models.BooleanField(default=True),
        ),
    ]
