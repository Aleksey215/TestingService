# Generated by Django 4.1.3 on 2022-12-11 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
