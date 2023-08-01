# Generated by Django 4.2.3 on 2023-08-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_store_app', '0009_alter_detail_address_alter_detail_age_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materials',
            options={'ordering': ['name'], 'verbose_name': 'material', 'verbose_name_plural': 'materials'},
        ),
        migrations.AlterModelOptions(
            name='purpose',
            options={'ordering': ['name'], 'verbose_name': 'purpose', 'verbose_name_plural': 'purposes'},
        ),
        migrations.AlterField(
            model_name='detail',
            name='dob',
            field=models.DateField(),
        ),
    ]