# Generated by Django 2.1.4 on 2018-12-10 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_ordergooditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergooditem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order'),
        ),
    ]
