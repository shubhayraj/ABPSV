# Generated by Django 3.0.7 on 2020-08-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_auto_20200612_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=100)),
                ('Tid', models.CharField(max_length=15)),
                ('Tpass', models.CharField(max_length=20)),
            ],
        ),
    ]
