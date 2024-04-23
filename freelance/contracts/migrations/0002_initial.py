# Generated by Django 5.0.4 on 2024-04-23 12:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contracts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="contractmodel",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="placed_contracts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Customer",
            ),
        ),
        migrations.AddField(
            model_name="contractmodel",
            name="performer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="completed_contracts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Performer",
            ),
        ),
    ]
