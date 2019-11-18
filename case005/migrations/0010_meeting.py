# Generated by Django 2.2.6 on 2019-11-18 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0009_merge_20191107_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('member', models.CharField(choices=[('Member', 'Member'), ('Guest', 'Guest')], max_length=6, verbose_name='Member or Guest')),
                ('date1', models.DateField(default=datetime.date.today, verbose_name='Meeting Date')),
                ('role', models.CharField(choices=[('Attendance', 'Attendance'), ('Ah-counter', 'Ah-counter'), ('GE', 'GE'), ('Grammarian', 'Grammarian'), ('IE', 'IE'), ('Speaker', 'Speaker'), ('TME', 'TME'), ('TT Speaker', 'TT Speaker'), ('TT Evaluator', 'TT Evaluator'), ('TT-master', 'TT-master'), ('Timer', 'Timer')], max_length=32, verbose_name='Meeting Role')),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Meeting V2',
                'verbose_name_plural': 'Meeting V2',
                'unique_together': {('name', 'date1', 'member', 'role')},
            },
        ),
    ]
