# Generated by Django 2.1.7 on 2019-03-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190305_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
