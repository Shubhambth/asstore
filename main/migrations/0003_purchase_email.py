# Generated by Django 5.1.3 on 2024-11-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.EmailField(default='shubham@gmail.com', max_length=254),
        ),
    ]
