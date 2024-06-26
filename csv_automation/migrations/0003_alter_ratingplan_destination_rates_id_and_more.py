# Generated by Django 5.0.6 on 2024-05-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_automation', '0002_alter_ratingplan_id_alter_testrate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingplan',
            name='destination_rates_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ratingplan',
            name='timing_tag',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ratingplan',
            name='weight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='destination_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='max_cost',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='max_cost_strategy',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='rates_tag',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='rounding_decimals',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='rounding_method',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
