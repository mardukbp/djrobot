# Generated by Django 4.2.3 on 2023-07-21 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotkw', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyword',
            old_name='doc',
            new_name='documentation',
        ),
    ]