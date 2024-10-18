# Generated by Django 4.2.16 on 2024-10-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_name', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=100, null=True)),
                ('manufacturer', models.CharField(max_length=100, null=True)),
                ('purchased_On', models.DateField(null=True)),
                ('owned_by', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('maintenance_date', models.DateField(null=True)),
            ],
        ),
    ]
