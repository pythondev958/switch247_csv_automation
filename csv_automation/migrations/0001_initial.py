# Generated by Django 5.0.6 on 2024-05-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_rates_id', models.CharField(max_length=40)),
                ('timing_tag', models.CharField(max_length=40)),
                ('weight', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TestRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_id', models.CharField(max_length=40)),
                ('rates_tag', models.CharField(max_length=40)),
                ('rounding_method', models.CharField(max_length=40)),
                ('rounding_decimals', models.CharField(max_length=40)),
                ('max_cost', models.CharField(max_length=40)),
                ('max_cost_strategy', models.CharField(max_length=40)),
            ],
        ),
    ]
