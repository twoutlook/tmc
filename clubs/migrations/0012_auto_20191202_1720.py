# Generated by Django 2.2.6 on 2019-12-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_person_teamnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='code',
            field=models.CharField(default='w00', max_length=3),
        ),
        migrations.AddField(
            model_name='person',
            name='email_checked',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
