# Generated by Django 4.2.3 on 2023-07-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testspec', '0004_alter_testcase_test_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordcall',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyword_calls', to='testspec.testcase'),
        ),
        migrations.AlterField(
            model_name='keywordcallargument',
            name='keyword_call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='args', to='testspec.keywordcall'),
        ),
        migrations.AlterField(
            model_name='keywordcalloptionalargument',
            name='keyword_call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kwargs', to='testspec.keywordcall'),
        ),
    ]
