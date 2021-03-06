# Generated by Django 2.2 on 2020-11-12 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bibliovirtual', '0006_merge_20201112_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='anio',
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='curso',
            name='division',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1),
        ),
    ]
