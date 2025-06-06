# Generated by Django 5.2 on 2025-05-21 07:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(choices=[('1', '1th'), ('2', '2th'), ('3', '3th'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th'), ('11', '11th'), ('12', '12th')], max_length=2)),
                ('medium', models.CharField(blank=True, choices=[('english', 'English'), ('marathi', 'Marathi'), ('semi', 'Semi-English')], max_length=10, null=True)),
                ('stream', models.CharField(blank=True, default='Commerce', max_length=20, null=True)),
                ('optional_subject_1', models.CharField(blank=True, choices=[('it', 'IT'), ('marathi', 'Marathi'), ('hindi', 'Hindi')], max_length=10, null=True)),
                ('optional_subject_2', models.CharField(blank=True, choices=[('maths', 'Maths'), ('sp', 'SP')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
