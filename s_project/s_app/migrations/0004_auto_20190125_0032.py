# Generated by Django 2.1.5 on 2019-01-25 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_app', '0003_auto_20190125_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='swe',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='s_app.Swe'),
        ),
    ]