# Generated by Django 4.2.3 on 2023-07-07 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0002_alter_keywordcall_arg1_alter_keywordcall_arg2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('arg1', models.CharField(blank=True, max_length=255)),
                ('arg2', models.CharField(blank=True, max_length=255)),
                ('arg3', models.CharField(blank=True, max_length=255)),
                ('arg4', models.CharField(blank=True, max_length=255)),
                ('arg5', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='keywordcall',
            name='arg1',
        ),
        migrations.RemoveField(
            model_name='keywordcall',
            name='arg2',
        ),
        migrations.RemoveField(
            model_name='keywordcall',
            name='arg3',
        ),
        migrations.RemoveField(
            model_name='keywordcall',
            name='arg4',
        ),
        migrations.RemoveField(
            model_name='keywordcall',
            name='arg5',
        ),
        migrations.AlterField(
            model_name='keywordcall',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.keyword'),
        ),
    ]
