# Generated by Django 3.1.2 on 2020-12-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books2', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='pics/'),
        ),
    ]
