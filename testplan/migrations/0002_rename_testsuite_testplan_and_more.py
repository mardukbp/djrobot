# Generated by Django 4.2.3 on 2023-07-23 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testplan', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestSuite',
            new_name='TestPlan',
        ),
        migrations.RenameField(
            model_name='libraryimport',
            old_name='test_suite',
            new_name='test_plan',
        ),
    ]
