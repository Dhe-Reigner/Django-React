# Generated by Django 5.1.4 on 2024-12-10 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BACKEND', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
    ]
