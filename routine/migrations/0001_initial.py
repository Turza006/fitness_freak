# Generated by Django 2.2.7 on 2019-11-18 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=2000, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_Catagory', models.CharField(max_length=1000)),
                ('s_id', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('sets', models.CharField(blank=True, max_length=10, null=True)),
                ('repetitions', models.CharField(blank=True, max_length=10, null=True)),
                ('rest_time', models.CharField(blank=True, max_length=10, null=True)),
                ('img1Path', models.ImageField(blank=True, null=True, upload_to='')),
                ('img2Path', models.ImageField(blank=True, null=True, upload_to='')),
                ('instruction', models.CharField(blank=True, max_length=10, null=True)),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.Sub_Category')),
            ],
        ),
    ]
