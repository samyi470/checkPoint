# Generated by Django 3.1.6 on 2021-06-27 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkPointMng', '0019_laxyear'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LAXMonth',
        ),
        migrations.DeleteModel(
            name='LAXYear',
        ),
    ]
