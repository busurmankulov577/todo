# Generated by Django 3.1.3 on 2021-01-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210120_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]