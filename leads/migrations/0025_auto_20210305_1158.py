# Generated by Django 3.1.2 on 2021-03-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0024_auto_20201111_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
    ]
