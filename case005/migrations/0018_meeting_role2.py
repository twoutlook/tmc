# Generated by Django 2.2.6 on 2019-11-18 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0017_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='role2',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='case005.Role'),
        ),
    ]