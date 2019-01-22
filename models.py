# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Events(models.Model):
    swe_email = models.ForeignKey('Swe', models.DO_NOTHING, db_column='swe_email')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event_created = models.DateTimeField()
    teamlead_user_email = models.ForeignKey('Teamlead', models.DO_NOTHING, db_column='teamlead_user_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'events'
        unique_together = (('teamlead_user_email', 'event_created'),)


class Manager(models.Model):
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_create_time = models.DateTimeField()
    swe_user_email = models.ForeignKey('Swe', models.DO_NOTHING, db_column='swe_user_email')
    teamlead_user_email = models.ForeignKey('Teamlead', models.DO_NOTHING, db_column='teamlead_user_email')
    team_name = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_name')

    class Meta:
        managed = False
        db_table = 'request'
        unique_together = (('request_id', 'swe_user_email', 'teamlead_user_email', 'team_name'),)


class Swe(models.Model):
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email', primary_key=True)
    team_name = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_name')
    teamlead_user_email = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamlead_user_email')

    class Meta:
        managed = False
        db_table = 'swe'


class Team(models.Model):
    name = models.IntegerField(primary_key=True)
    teamlead_user_email = models.ForeignKey('Teamlead', models.DO_NOTHING, db_column='teamlead_user_email')
    max_swes_out = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
        unique_together = (('name', 'teamlead_user_email'),)


class Teamlead(models.Model):
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'teamlead'


class User(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=128)
    create_time = models.DateTimeField(blank=True, null=True)
    time_zone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
