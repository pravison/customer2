# Generated by Django 4.2.4 on 2023-10-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='business_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]