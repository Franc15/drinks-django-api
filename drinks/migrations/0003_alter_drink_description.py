# Generated by Django 4.1.4 on 2022-12-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_remove_drink_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]