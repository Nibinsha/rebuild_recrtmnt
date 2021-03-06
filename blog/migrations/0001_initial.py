# Generated by Django 3.2.5 on 2021-10-01 08:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('industry_type', models.CharField(max_length=250, null=True)),
                ('country', models.CharField(max_length=250)),
                ('address1', models.CharField(max_length=250, null=True)),
                ('address2', models.CharField(max_length=250, null=True)),
                ('state', models.CharField(max_length=250)),
                ('pin', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('primary_mob_no', models.CharField(max_length=15)),
                ('secondary_mob_no', models.CharField(blank=True, max_length=15, null=True)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('passport_no', models.CharField(blank=True, max_length=100, null=True)),
                ('passport_expery_date', models.DateField(blank=True, null=True)),
                ('licence_id', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('valid_up_to', models.DateField(blank=True, null=True)),
                ('job_category', models.CharField(blank=True, max_length=100, null=True)),
                ('total_experence', models.FloatField(blank=True, default=0.0, null=True)),
                ('abroad_experence', models.FloatField(blank=True, default=0.0, null=True)),
                ('document_files', models.FileField(blank=True, upload_to='documents/')),
                ('scheduled_on', models.DateField(blank=True, null=True)),
                ('duration_in_min', models.CharField(blank=True, max_length=50, null=True)),
                ('interview_status', models.CharField(blank=True, choices=[('schedule', 'SCHEDULE'), ('not_schedule', ' NOT SCHEDULE'), ('completed', 'COMPLETED'), ('seleted', 'SELECTED')], default='not_schedule', max_length=40, null=True)),
                ('visa_approval_status', models.BooleanField(default=False)),
                ('salary_details', models.TextField(blank=True, null=True)),
                ('passport_status', models.CharField(blank=True, choices=[('collected', 'COLLECTED'), ('not_collected', ' NOT COLLECTED')], max_length=40, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('added_date', models.DateField(auto_now=True, null=True)),
                ('intervew_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.clientmaster')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
