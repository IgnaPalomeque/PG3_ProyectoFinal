# Generated by Django 2.2 on 2020-11-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliovirtual', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libroenventa',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='libroenventa',
            name='foto_portada',
            field=models.ImageField(blank=True, upload_to='fotos_portada/'),
        ),
        migrations.AddField(
            model_name='materiadescargable',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfdescarga/'),
        ),
        migrations.AddField(
            model_name='material',
            name='descripcion',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
