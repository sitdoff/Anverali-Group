# Generated by Django 5.0.4 on 2024-04-23 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="usermodel",
            name="last_name",
        ),
    ]
