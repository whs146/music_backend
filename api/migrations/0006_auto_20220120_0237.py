# Generated by Django 3.1.7 on 2022-01-19 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220120_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='created_at',
            new_name='create_at',
        ),
    ]
