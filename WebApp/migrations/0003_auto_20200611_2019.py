# Generated by Django 3.0.7 on 2020-06-11 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20200611_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='BCand',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.BCand'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='GCand',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.GCand'),
        ),
    ]