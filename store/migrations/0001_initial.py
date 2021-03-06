# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status',
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username',
                                              help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                                                                'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
                                                                                                'invalid')],
                                              unique=True, max_length=30,
                                              error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status',
                                                 help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active',
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('qq', models.CharField(blank=True, verbose_name='QQ??????', max_length=20, null=True)),
                ('mobile', models.CharField(blank=True, unique=True, verbose_name='????????????', max_length=11, null=True)),
                ('address', models.CharField(blank=True, unique=True, verbose_name='????????????', max_length=50, null=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set',
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  blank=True, related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set',
                                                            help_text='Specific permissions for this user.', blank=True,
                                                            related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': '??????',
                'ordering': ['-id'],
                'verbose_name_plural': '??????',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='??????', max_length=50)),
                ('image_url', models.ImageField(verbose_name='????????????', upload_to='ad/%Y/%m')),
                ('date_publish', models.DateTimeField(verbose_name='????????????', auto_now_add=True)),
                ('index', models.IntegerField(default=1, verbose_name='????????????')),
            ],
            options={
                'verbose_name': '??????',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='????????????', max_length=30)),
                ('index', models.IntegerField(default=1, verbose_name='????????????')),
            ],
            options={
                'verbose_name': '??????',
                'ordering': ['index'],
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('typ', models.CharField(verbose_name='????????????', max_length=20)),
                ('name', models.CharField(verbose_name='????????????', max_length=30)),
                ('index', models.IntegerField(default=1, verbose_name='???????????????')),
                ('sex', models.IntegerField(default=0, verbose_name='??????')),
            ],
            options={
                'verbose_name': '??????',
                'ordering': ['index', 'id'],
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='??????', max_length=30)),
                ('old_price', models.FloatField(default=0.0, verbose_name='??????')),
                ('new_price', models.FloatField(default=0.0, verbose_name='??????')),
                ('discount', models.FloatField(default=1, verbose_name='??????')),
                ('desc', models.CharField(verbose_name='??????', max_length=100)),
                ('sales', models.IntegerField(default=0, verbose_name='??????')),
                ('num', models.IntegerField(default=0, verbose_name='??????')),
                ('image_url_i',
                 models.ImageField(default='clothing/default.jpg', verbose_name='??????????????????', upload_to='clothing/%Y/%m')),
                ('image_url_l',
                 models.ImageField(default='clothing/default.jpg', verbose_name='??????????????????1', upload_to='clothing/%Y/%m')),
                ('image_url_m',
                 models.ImageField(default='clothing/default.jpg', verbose_name='??????????????????2', upload_to='clothing/%Y/%m')),
                ('image_url_r',
                 models.ImageField(default='clothing/default.jpg', verbose_name='??????????????????3', upload_to='clothing/%Y/%m')),
                ('brand', models.ForeignKey(verbose_name='??????', to='store.Brand', on_delete=models.CASCADE)),
                ('category', models.ForeignKey(verbose_name='??????', to='store.Category', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': '??????',
                'ordering': ['id'],
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='??????', max_length=20)),
                ('index', models.IntegerField(default=1, verbose_name='????????????')),
            ],
            options={
                'verbose_name': '??????',
                'ordering': ['index'],
                'verbose_name_plural': '??????',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='??????', max_length=30)),
            ],
            options={
                'verbose_name': '??????',
                'verbose_name_plural': '??????',
            },
        ),
        migrations.AddField(
            model_name='clothing',
            name='size',
            field=models.ManyToManyField(verbose_name='??????', to='store.Size'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='tag',
            field=models.ManyToManyField(verbose_name='??????', to='store.Tag'),
        ),
    ]
