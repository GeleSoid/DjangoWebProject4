# Generated by Django 4.2.1 on 2023-05-27 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_blog_posted_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 27, 21, 5, 47, 95319), verbose_name='To publish'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 27, 21, 5, 47, 95319), verbose_name='Date of the comment'),
        ),
    ]
