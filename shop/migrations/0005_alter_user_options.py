# Generated by Django 4.2.7 on 2023-11-14 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('username',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]