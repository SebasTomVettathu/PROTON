# Generated by Django 5.0.1 on 2024-03-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_cpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_cpo',
            name='cpo_email',
            field=models.EmailField(max_length=50),
        ),
    ]
