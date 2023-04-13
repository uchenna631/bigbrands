# Generated by Django 3.2.16 on 2023-04-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_ordermanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermanager',
            name='delivered',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='ordermanager',
            name='delivered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordermanager',
            name='processed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='ordermanager',
            name='processed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
