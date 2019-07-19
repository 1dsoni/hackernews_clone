# Generated by Django 2.2.3 on 2019-07-19 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=200)),
                ('hackernews_url', models.URLField()),
                ('url', models.URLField(blank=True, null=True)),
                ('posted_age', models.TextField(max_length=50)),
                ('here_posted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('upvotes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('read_timestamp', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
