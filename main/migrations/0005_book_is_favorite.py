# Generated by Django 3.1.3 on 2021-01-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210120_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]