# Generated by Django 3.0.13 on 2021-04-04 12:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import racetime.validators


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0051_auto_20201215_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of your team. Must be unique and follow our naming guidelines.', max_length=25, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='Name cannot contain @ or #', regex='[\\x00@#]'), racetime.validators.UsernameValidator()])),
                ('slug', models.SlugField(help_text='Forms part of the URL of your team page, e.g. "your-team" will give "racetime.gg/team/your-team". Slug must be unique, and can only use letters, numbers and hyphens.', null=True, unique=True)),
                ('profile', models.TextField(blank=True, help_text="Add some information to your team's public profile. It can include anything you like.", null=True)),
                ('avatar', models.ImageField(blank=True, help_text='Recommended size: 100x100. No larger than 100kb.', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('max_owners', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)])),
                ('max_members', models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1000)])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='race',
            name='allow_prerace_chat',
            field=models.BooleanField(default=True, help_text='Allow users to chat before the race starts (race monitors can always use chat messages).', verbose_name='Allow pre-race chat'),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='action',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug_words',
            field=models.TextField(blank=True, default=None, help_text='Set a number of words to be picked at random for race room names. If set, you must provide a minimum of 50 distinct words to use. Add one word per line, no punctuation or numbers.', null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='allow_midrace_chat',
            field=models.BooleanField(default=True, help_text='Allow users to chat during the race (race monitors can always use chat messages).', verbose_name='Allow mid-race chat'),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.BooleanField(default=False)),
                ('invite', models.BooleanField(default=True)),
                ('invited_at', models.DateTimeField(null=True)),
                ('joined_at', models.DateTimeField(null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetime.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(db_index=True, max_length=255)),
                ('old_value', models.TextField(null=True)),
                ('new_value', models.TextField(null=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetime.Team')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='team',
            name='categories',
            field=models.ManyToManyField(to='racetime.Category'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='racetime.Team'),
        ),
    ]
