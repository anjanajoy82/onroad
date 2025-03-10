# Generated by Django 5.1.5 on 2025-02-25 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_name', models.CharField(max_length=50)),
                ('fuel_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('petrol_pump', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
