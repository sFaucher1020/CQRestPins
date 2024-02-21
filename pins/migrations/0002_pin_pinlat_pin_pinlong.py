# Generated by Django 4.2.10 on 2024-02-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='pinLat',
            field=models.DecimalField(decimal_places=15, default=0.0, max_digits=17),
        ),
        migrations.AddField(
            model_name='pin',
            name='pinLong',
            field=models.DecimalField(decimal_places=15, default=0.0, max_digits=17),
        ),
    ]
