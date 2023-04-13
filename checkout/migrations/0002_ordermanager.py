# Generated by Django 3.2.16 on 2023-04-13 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processed', models.BooleanField(default=False)),
                ('processed_by', models.CharField(blank=True, max_length=120)),
                ('processed_date', models.DateTimeField(blank=True)),
                ('delivered', models.BooleanField(default=False)),
                ('delivered_by', models.CharField(blank=True, max_length=120)),
                ('delivered_date', models.DateTimeField(blank=True)),
                ('status', models.CharField(blank=True, max_length=80)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
