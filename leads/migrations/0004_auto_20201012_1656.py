# Generated by Django 3.1.2 on 2020-10-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_lead_logo'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='lead',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
