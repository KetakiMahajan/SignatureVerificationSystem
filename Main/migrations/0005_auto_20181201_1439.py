# Generated by Django 2.1 on 2018-12-01 09:09

import Main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20181201_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='customerdetails',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='image',
            field=models.FileField(default='hi', upload_to=Main.models.user_directory),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]