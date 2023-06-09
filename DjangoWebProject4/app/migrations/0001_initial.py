# Generated by Django 4.2.1 on 2023-05-26 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Title')),
                ('description', models.TextField(verbose_name='Summary')),
                ('content', models.TextField(verbose_name='Full content')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 26, 12, 10, 17, 82654), verbose_name='To publish')),
            ],
            options={
                'verbose_name': 'blog article',
                'verbose_name_plural': 'blog article',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
