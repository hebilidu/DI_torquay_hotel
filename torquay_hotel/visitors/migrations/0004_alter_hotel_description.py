# Generated by Django 3.2.3 on 2021-06-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_alter_room_rate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(),
        ),
    ]
