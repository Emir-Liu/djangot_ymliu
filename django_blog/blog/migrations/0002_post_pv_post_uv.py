# Generated by Django 5.0.6 on 2024-06-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="pv",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="post",
            name="uv",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
