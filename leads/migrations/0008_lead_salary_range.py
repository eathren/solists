# Generated by Django 3.1.2 on 2020-11-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20201028_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='salary_range',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
