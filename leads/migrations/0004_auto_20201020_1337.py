# Generated by Django 3.1.2 on 2020-10-20 17:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_lead_application_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]