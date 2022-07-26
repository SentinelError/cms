# Generated by Django 4.0.5 on 2022-07-21 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App2', '0014_event_event_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='overseer',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='Overseer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Attendees', to='App2.venue'),
        ),
    ]
