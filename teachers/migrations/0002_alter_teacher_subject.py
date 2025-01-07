# Generated by Django 5.1.4 on 2025-01-07 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subject', to='subjects.subject'),
        ),
    ]
