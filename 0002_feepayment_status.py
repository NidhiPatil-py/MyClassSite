# Generated by Django 5.2 on 2025-05-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feepayment',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
