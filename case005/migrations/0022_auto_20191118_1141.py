# Generated by Django 2.2.6 on 2019-11-18 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0021_auto_20191118_1122'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together={('name', 'date1', 'role')},
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='member',
        ),
    ]
