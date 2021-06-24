# Generated by Django 3.1.6 on 2021-06-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkPointMng', '0014_lasday_twentyfifteen'),
    ]

    operations = [
        migrations.CreateModel(
            name='LAXDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal', models.CharField(choices=[('Suites', 'Suites'), ('TBIT Main Checkpoint', 'TBIT Main Checkpoint'), ('Terminal 1 - Passenger', 'Terminal 1 - Passenger'), ('Terminal 2 - Passenger', 'Terminal 2 - Passenger'), ('Terminal 3 - Passenger', 'Terminal 3 - Passenger'), ('Terminal 4 - FIS', 'Terminal 4 - FIS'), ('Terminal 4 - Passenger', 'Terminal 4 - Passenger'), ('Terminal 4a - Passenger', 'Terminal 4a - Passenger'), ('Terminal 5 - Passenger', 'Terminal 5 - Passenger'), ('Terminal 5a - Passenger', 'Terminal 5a - Passenger'), ('Terminal 6 - Passenger', 'Terminal 6 - Passenger'), ('Terminal 7 - Passenger', 'Terminal 7 - Passenger')], max_length=23)),
                ('primary', models.DateField()),
                ('twentyTwenty', models.BooleanField(default=False, verbose_name='2020')),
                ('twentyNineteen', models.BooleanField(default=False, verbose_name='2019')),
                ('twentyEighteen', models.BooleanField(default=False, verbose_name='2018')),
                ('twentySeventeen', models.BooleanField(default=False, verbose_name='2017')),
                ('twentySixteen', models.BooleanField(default=False, verbose_name='2016')),
                ('twentyFifteen', models.BooleanField(default=False, verbose_name='2015')),
            ],
        ),
    ]
