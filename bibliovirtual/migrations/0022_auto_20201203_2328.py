# Generated by Django 2.2 on 2020-12-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliovirtual', '0021_auto_20201203_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='titulo',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]