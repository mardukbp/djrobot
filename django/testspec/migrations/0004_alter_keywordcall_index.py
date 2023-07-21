# Generated by Django 4.2.3 on 2023-07-21 15:53

from django.db import migrations, models
import testspec.models


class Migration(migrations.Migration):

    dependencies = [
        ('testspec', '0003_alter_testcase_documentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordcall',
            name='index',
            field=models.PositiveSmallIntegerField(db_index=True, default=testspec.models.next_keywordcall_index),
        ),
    ]
