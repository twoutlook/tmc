# Generated by Django 2.2.6 on 2019-11-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0006_auto_20191107_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data2',
            name='member',
            field=models.CharField(choices=[('Member', 'Member'), ('Guest', 'Guest')], max_length=6, verbose_name='Member or Guest'),
        ),
    ]
