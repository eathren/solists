# Generated by Django 3.1.2 on 2020-10-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_lead_user_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logos/'),
        ),
    ]
