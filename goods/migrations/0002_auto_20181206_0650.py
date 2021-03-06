# Generated by Django 2.1.4 on 2018-12-06 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.Shop'),
        ),
        migrations.AlterField(
            model_name='good',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
