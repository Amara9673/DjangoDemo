# Generated by Django 5.1.4 on 2024-12-10 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='I love tacobell'),
        ),
    ]
