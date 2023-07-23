# Generated by Django 4.2.3 on 2023-07-23 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robotlib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initargument',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='robotlib.library'),
        ),
        migrations.AlterField(
            model_name='keywordargument',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='args', to='robotlib.librarykeyword'),
        ),
        migrations.AlterField(
            model_name='keywordoptionalargument',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kwargs', to='robotlib.librarykeyword'),
        ),
        migrations.AlterField(
            model_name='librarykeyword',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='robotlib.library'),
        ),
        migrations.AddConstraint(
            model_name='library',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_library'),
        ),
    ]