# Generated by Django 3.2.16 on 2023-10-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20230413_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.TextField(default='processing'),
        ),
        migrations.DeleteModel(
            name='OrderManager',
        ),
    ]
