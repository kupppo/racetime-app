# Generated by Django 3.2.20 on 2023-09-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0062_auto_20230806_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='actions',
            field=models.JSONField(blank=True, default={}),
        ),
        migrations.AddField(
            model_name='message',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
