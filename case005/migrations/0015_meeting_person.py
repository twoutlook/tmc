# Generated by Django 2.2.6 on 2019-11-18 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0014_person_personclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='case005.Person'),
        ),
    ]
