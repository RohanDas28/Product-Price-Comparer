# Generated by Django 3.2 on 2021-07-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommercePriceComparer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=25),
        ),
    ]