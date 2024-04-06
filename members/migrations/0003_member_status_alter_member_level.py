# Generated by Django 5.0.3 on 2024-04-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('RETIRED', 'Retired'), ('EMERITUSEmeritus', 'Emeritus')], default='ACTIVE', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.CharField(choices=[('CANDIDATE', 'Candidate'), ('JUNIOR', 'Junior'), ('MIDDLE_SCHOOL', 'Middle School'), ('JUNIOR_VARSITY', 'Junior Varsity'), ('VARSITY', 'Varsity')], default='CANDIDATE', max_length=20),
        ),
    ]
