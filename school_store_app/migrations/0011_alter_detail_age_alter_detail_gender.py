# Generated by Django 4.2.3 on 2023-08-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_store_app', '0010_alter_materials_options_alter_purpose_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=128),
        ),
    ]
