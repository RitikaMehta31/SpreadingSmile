# Generated by Django 3.1.2 on 2020-10-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201020_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteermodel',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
