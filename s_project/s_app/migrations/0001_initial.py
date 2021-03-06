# Generated by Django 2.1.5 on 2019-01-23 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import s_app.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('type', models.CharField(choices=[('s', 'Shift'), ('m', 'Meeting'), ('v', 'Vacation'), ('f', 'Floating Holiday'), ('i', 'Ill/Sick'), ('p', 'Personal')], default='s', help_text='Type of Event', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TYPE', models.CharField(choices=[('v', 'Vacation'), ('f', 'Floating Holiday'), ('i', 'Ill/Sick'), ('p', 'Personal')], default='v', help_text='Reason for Time-Off Request', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Swe',
            fields=[
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teamlead',
            fields=[
                ('user_email', models.ForeignKey(on_delete=models.SET(s_app.models.get_new_teamlead), primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='s_app.Teamlead'),
        ),
        migrations.AddField(
            model_name='swe',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='s_app.Team'),
        ),
        migrations.AddField(
            model_name='request',
            name='swe_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='s_app.Swe'),
        ),
        migrations.AddField(
            model_name='event',
            name='swe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='s_app.Swe'),
        ),
    ]
