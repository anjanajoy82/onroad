# Generated by Django 5.1.5 on 2025-02-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechbooking',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
