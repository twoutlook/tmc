# Generated by Django 2.2.6 on 2019-11-18 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0019_person_member_since'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
