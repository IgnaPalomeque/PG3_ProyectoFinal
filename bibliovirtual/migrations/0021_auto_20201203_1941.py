# Generated by Django 2.2 on 2020-12-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliovirtual', '0020_auto_20201203_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libroenventa',
            name='vendedor',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
