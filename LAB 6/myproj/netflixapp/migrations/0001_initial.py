# Generated by Django 3.2.9 on 2021-11-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('director', models.CharField(blank=True, max_length=1000)),
                ('country', models.CharField(blank=True, max_length=1000)),
                ('cast', models.CharField(blank=True, max_length=1000)),
                ('date_added', models.DateField(blank=True)),
                ('release_year', models.IntegerField(blank=True)),
                ('rating', models.CharField(blank=True, max_length=1000)),
                ('duration', models.CharField(blank=True, max_length=1000)),
                ('listed_in', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
