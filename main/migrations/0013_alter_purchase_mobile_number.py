# Generated by Django 5.1.3 on 2024-11-21 04:59

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_purchase_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='mobile_number',
            field=models.CharField(default='0000000000', max_length=10, validators=[main.models.validate_mobile_number]),
        ),
    ]