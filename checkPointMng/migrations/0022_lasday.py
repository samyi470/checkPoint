# Generated by Django 3.1.6 on 2021-07-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkPointMng', '0021_auto_20210627_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='LASDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal', models.CharField(choices=[('Term 1 - AB', 'Term 1 - AB'), ('Term 1 - C', 'Term 1 - C'), ('Term 1 - CX', 'Term 1 - CX'), ('Term 1 - D', 'Term 1 - D'), ('Terminal 3 - E Lower (1)', 'Terminal 3 - E Lower (1)'), ('Terminal 3 - E Upper', 'Terminal 3 - E Upper')], max_length=24)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
    ]