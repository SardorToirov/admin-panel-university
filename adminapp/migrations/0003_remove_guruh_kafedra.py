# Generated by Django 4.0.6 on 2025-03-08 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_remove_kafedra_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guruh',
            name='kafedra',
        ),
    ]
