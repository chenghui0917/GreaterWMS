# Generated by Django 3.1.3 on 2020-11-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listmodel',
            name='unit_volum',
            field=models.FloatField(default=0, verbose_name='Unit Volume'),
        ),
    ]
