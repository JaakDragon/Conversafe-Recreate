# Generated by Django 5.0.5 on 2024-09-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_userprofile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]
