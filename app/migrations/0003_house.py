# Generated by Django 4.0.3 on 2022-09-29 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_housestatus_housetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, default='Country | State', max_length=200, null=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('no_of_bedrooms', models.IntegerField()),
                ('area_per_meter_square', models.IntegerField()),
                ('no_of_bathroom', models.IntegerField()),
                ('garage', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('deck', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('outdoor_kitchen', models.BooleanField(default=False)),
                ('tennis_court', models.BooleanField(default=False)),
                ('sun_room', models.BooleanField(default=False)),
                ('cable_tv', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('concrete_flooring', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('house_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.housetype')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.housestatus')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
