# Generated by Django 4.2.1 on 2023-05-26 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 26, 12, 32, 32, 79730), verbose_name='To publish'),
        ),
    ]
