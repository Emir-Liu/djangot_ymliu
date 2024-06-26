# Generated by Django 5.0.6 on 2024-06-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sidebar",
            name="display_type",
            field=models.PositiveIntegerField(
                choices=[(1, "展示"), (0, "隐藏")], default=1, verbose_name="展示类型"
            ),
        ),
        migrations.AlterField(
            model_name="sidebar",
            name="status",
            field=models.PositiveIntegerField(
                choices=[(1, "展示"), (0, "隐藏")], default=1, verbose_name="状态"
            ),
        ),
    ]
