# Generated by Django 4.2.3 on 2023-07-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testspec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='documentation',
            field=models.TextField(default=''),
        ),
    ]