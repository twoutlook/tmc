# Generated by Django 2.2.6 on 2019-11-01 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case005', '0002_auto_20191101_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data2',
            name='role',
            field=models.CharField(choices=[('Ah-counter', 'Ah-counter'), ('Attendance', 'Attendance'), ('GE', 'GE'), ('Grammarian', 'SenGrammarianior'), ('IE', 'IE'), ('Speaker', 'Speaker'), ('TME', 'TME'), ('TT Evaluator', 'TT Evaluator'), ('TT-master', 'TT-master'), ('Timer', 'Timer')], max_length=32),
        ),
        migrations.AlterUniqueTogether(
            name='data2',
            unique_together={('name', 'date1', 'member', 'role')},
        ),
    ]
