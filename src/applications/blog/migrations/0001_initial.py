# Generated by Django 3.1.4 on 2020-12-05 18:57

from django.db import migrations
from django.db import models

import applications.blog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(blank=True, null=True)),
                ("nr_likes", models.IntegerField(default=0)),
                ("nr_views", models.IntegerField(default=0)),
                (
                    "created_at",
                    models.DateTimeField(default=applications.blog.models._now),
                ),
                ("edited", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
