# Generated by Django 5.0.1 on 2024-05-09 11:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royaldrive', '0006_alter_favouriteitem_car_object'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=200, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('booked', 'booked'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='booked', max_length=200)),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_item_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='royaldrive.favouriteitem')),
                ('order_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseitems', to='royaldrive.order')),
            ],
        ),
    ]
