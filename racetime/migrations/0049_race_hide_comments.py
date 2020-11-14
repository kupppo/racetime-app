# Generated by Django 3.0.11 on 2020-11-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0048_auto_20201114_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='hide_comments',
            field=models.BooleanField(default=False, help_text='Do not show comments until the race has finished. Has no effect if comments are not enabled (duh!).'),
        ),
    ]
