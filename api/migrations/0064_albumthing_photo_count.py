# Generated by Django 4.2.11 on 2024-03-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0063_apply_default_album_things_cover"),
    ]

    operations = [
        migrations.AddField(
            model_name="albumthing",
            name="photo_count",
            field=models.IntegerField(default=0),
        ),
    ]
