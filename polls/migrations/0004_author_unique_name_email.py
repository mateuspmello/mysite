# Generated by Django 4.2.10 on 2024-03-01 12:49

from django.db import migrations, models
from rest_framework import serializers

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post_author'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('name', 'email'), name='unique_name_email'),
        ),
    ]
