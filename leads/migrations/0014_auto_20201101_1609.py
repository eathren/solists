# Generated by Django 3.1.2 on 2020-11-01 21:09

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_auto_20201101_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='country',
            field=django_countries.fields.CountryField(blank=True, help_text='Test', max_length=2),
        ),
    ]
