# Generated by Django 3.2.4 on 2021-06-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impression', '0002_impression_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impression',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Координаты места'),
        ),
    ]
