# Generated by Django 2.2.6 on 2019-12-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_auto_20191201_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='member_num',
            field=models.CharField(default='---', max_length=32),
        ),
    ]
