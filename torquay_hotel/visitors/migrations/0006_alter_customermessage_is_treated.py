# Generated by Django 3.2.3 on 2021-06-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0005_auto_20210603_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermessage',
            name='is_treated',
            field=models.BooleanField(default=0),
        ),
    ]
