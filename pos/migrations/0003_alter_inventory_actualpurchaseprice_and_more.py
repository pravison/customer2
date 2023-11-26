# Generated by Django 4.2.4 on 2023-09-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_remove_inventory_type_inventory_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='ActualPurchasePrice',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='ActualSalePrice',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='currentValue',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='discountGiven',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='discountReceived',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='expectedLifespan',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='forSale',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inventoryType',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='leased',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='measurementUnit',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='monthlyFees',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='purchasePrice',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='salePrice',
            field=models.FloatField(default=0),
        ),
    ]
