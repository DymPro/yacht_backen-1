# Generated by Django 3.2.18 on 2023-05-26 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_companymanual_poistion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companymanual',
            old_name='poistion',
            new_name='position',
        ),
    ]