# Generated by Django 2.2 on 2020-12-01 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bibliovirtual', '0018_delete_materia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliovirtual.Curso')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
