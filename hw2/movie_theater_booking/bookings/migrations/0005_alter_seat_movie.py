# Generated by Django 4.2.11 on 2025-03-03 00:15

import bookings.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_seat_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(blank=True, default=bookings.models.get_default_movie, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.movie'),
        ),
    ]
