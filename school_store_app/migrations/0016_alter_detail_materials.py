# Generated by Django 4.2.3 on 2023-08-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_store_app', '0015_alter_detail_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='materials',
            field=models.BigIntegerField(),
        ),
    ]