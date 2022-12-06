# Generated by Django 4.1.4 on 2022-12-06 22:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auto_parks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoparkmodel',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='auto_parks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
