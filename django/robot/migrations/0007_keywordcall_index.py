# Generated by Django 4.2.3 on 2023-07-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0006_alter_library_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordcall',
            name='index',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]