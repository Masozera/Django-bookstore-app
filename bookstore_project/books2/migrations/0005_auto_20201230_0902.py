# Generated by Django 3.1.2 on 2020-12-30 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books2', '0004_auto_20201230_0622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
