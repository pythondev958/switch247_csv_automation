# Generated by Django 5.0.6 on 2024-05-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_automation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingplan',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testrate',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]