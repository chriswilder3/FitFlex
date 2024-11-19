# Generated by Django 5.1.3 on 2024-11-18 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message='Phone no must be exact 10 digits', regex='^\\d{10}')])),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]