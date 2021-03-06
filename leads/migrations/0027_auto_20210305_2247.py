# Generated by Django 3.1.2 on 2021-03-06 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0026_auto_20210305_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='user_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
