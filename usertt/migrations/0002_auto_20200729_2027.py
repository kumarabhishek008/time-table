# Generated by Django 3.0.5 on 2020-07-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetablecolumn',
            name='row',
            field=models.IntegerField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth'), ('fifth', 'fifth'), ('sixth', 'sixth'), ('seventh', 'seventh')], default=0),
        ),
    ]
