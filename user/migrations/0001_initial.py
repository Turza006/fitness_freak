# Generated by Django 2.2.7 on 2019-11-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('pro_pic', models.ImageField(upload_to='')),
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]