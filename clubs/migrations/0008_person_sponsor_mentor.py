# Generated by Django 2.2.6 on 2019-12-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_auto_20191201_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sponsor_mentor',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]