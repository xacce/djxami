# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db.migrations.migration import SwappableTuple


def swappable_dependency_latest(value):
    """
    Turns a setting value into a dependency.
    """
    return SwappableTuple((value.split(".", 1)[0], "__latest__"), value)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '__latest__'),
        ('auth', '__latest__'),
        swappable_dependency_latest(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mark_as_viewed_at', models.DateTimeField(blank=True, null=True)),
                ('globally', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='MessageToGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djxami.Message')),
            ],
        ),
        migrations.CreateModel(
            name='MessageToUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed', models.BooleanField(default=False)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to_user', to='djxami.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='groups',
            field=models.ManyToManyField(through='djxami.MessageToGroup', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='message',
            name='users',
            field=models.ManyToManyField(through='djxami.MessageToUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='message',
            index_together=set([('content_type', 'object_id')]),
        ),
    ]
