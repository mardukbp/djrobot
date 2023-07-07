# Generated by Django 4.2.3 on 2023-07-07 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0008_keywordcall_unique_keyword_call_per_test_case'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Library', 'Library')], default='Library', max_length=255)),
                ('arg1', models.CharField(blank=True, max_length=255)),
                ('arg2', models.CharField(blank=True, max_length=255)),
                ('arg3', models.CharField(blank=True, max_length=255)),
                ('arg4', models.CharField(blank=True, max_length=255)),
                ('arg5', models.CharField(blank=True, max_length=255)),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.testsuite')),
            ],
        ),
    ]
