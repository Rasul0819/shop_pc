# Generated by Django 4.2.7 on 2023-11-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_num',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
