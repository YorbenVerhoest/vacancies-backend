# Generated by Django 4.2.9 on 2024-01-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_conditiontypes_conditiontype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
