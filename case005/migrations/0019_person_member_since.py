# Generated by Django 2.2.6 on 2019-11-18 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0018_meeting_role2'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='member_since',
            field=models.DateField(blank=True, null=True, verbose_name='Member Since'),
        ),
    ]