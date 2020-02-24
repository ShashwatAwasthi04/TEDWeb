# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-28 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorApplicationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('domain', models.CharField(max_length=150)),
                ('POC', models.CharField(max_length=150)),
                ('contactNo', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('status', models.IntegerField(choices=[(1, b'Applied'), (2, b'Reviewing'), (3, b'Accepted'), (4, b'Rejected')])),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('domain', models.CharField(max_length=150)),
                ('Website', models.URLField(max_length=256)),
                ('Image', models.ImageField(upload_to=b'')),
                ('is_previous', models.BooleanField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
