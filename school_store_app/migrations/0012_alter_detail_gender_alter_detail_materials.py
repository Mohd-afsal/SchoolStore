# Generated by Django 4.2.3 on 2023-08-01 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_store_app', '0011_alter_detail_age_alter_detail_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='detail',
            name='materials',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_store_app.materials'),
        ),
    ]
