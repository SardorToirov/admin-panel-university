# Generated by Django 4.0.6 on 2025-03-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_remove_guruh_kafedra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, default='images/img.png', null=True, upload_to='images'),
        ),
    ]
