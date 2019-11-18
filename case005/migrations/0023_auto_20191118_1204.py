# Generated by Django 2.2.6 on 2019-11-18 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0022_auto_20191118_1141'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together={('person', 'date1', 'role2')},
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='name',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='points',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='role',
        ),
    ]
