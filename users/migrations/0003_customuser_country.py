# Generated by Django 3.1.2 on 2020-10-18 19:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201018_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(default='NZ', max_length=2),
            preserve_default=False,
        ),
    ]
