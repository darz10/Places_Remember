# Generated by Django 3.2.4 on 2021-06-15 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('impression', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.profile'),
        ),
    ]
