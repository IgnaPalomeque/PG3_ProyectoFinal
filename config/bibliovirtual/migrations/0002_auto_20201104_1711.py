# Generated by Django 2.2 on 2020-11-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliovirtual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='anio',
            field=models.CharField(choices=[('1', '1ero'), ('2', '2do'), ('3', '3ero'), ('4', '4to'), ('5', '5to'), ('6', '6to'), ('7', '7mo')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='division',
            field=models.CharField(choices=[('A', '°A'), ('B', '°B'), ('C', '°C')], max_length=10),
        ),
    ]
