# Generated by Django 3.1.1 on 2020-09-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('score1', models.CharField(max_length=10)),
                ('score2', models.CharField(max_length=10)),
                ('score3', models.CharField(max_length=10)),
            ],
        ),
    ]
