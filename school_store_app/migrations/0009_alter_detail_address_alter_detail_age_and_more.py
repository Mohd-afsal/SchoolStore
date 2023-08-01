# Generated by Django 4.2.3 on 2023-08-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_store_app', '0008_alter_detail_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='address',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='detail',
            name='age',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='detail',
            name='phone_number',
            field=models.PositiveBigIntegerField(),
        ),
    ]
