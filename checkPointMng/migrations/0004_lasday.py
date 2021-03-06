# Generated by Django 3.1.6 on 2021-06-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkPointMng', '0003_auto_20210611_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='LASDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal', models.CharField(max_length=200, unique=True)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('week', models.DecimalField(decimal_places=0, max_digits=2)),
                ('day', models.CharField(max_length=7)),
            ],
        ),
    ]
