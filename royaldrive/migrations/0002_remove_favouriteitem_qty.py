# Generated by Django 5.0.1 on 2024-03-16 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('royaldrive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouriteitem',
            name='qty',
        ),
    ]
