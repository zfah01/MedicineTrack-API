# Generated by Django 4.2.17 on 2024-12-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_alter_medicine_batch_number_alter_medicine_dosage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='batch_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='dosage',
            field=models.CharField(max_length=100),
        ),
    ]
