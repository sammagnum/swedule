# Generated by Django 2.1.5 on 2019-01-25 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_app', '0006_auto_20190125_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swe',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
