# Generated by Django 2.2 on 2020-11-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliovirtual', '0003_curso_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='title',
        ),
    ]