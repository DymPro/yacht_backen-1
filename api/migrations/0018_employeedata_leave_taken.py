# Generated by Django 4.1.7 on 2023-03-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_leave_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedata',
            name='leave_taken',
            field=models.IntegerField(default=0),
        ),
    ]
