# Generated by Django 2.2 on 2020-11-02 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('materia', models.CharField(choices=[('L', 'Lengua'), ('B', 'Biologia'), ('M', 'Matematica'), ('I', 'Ingles'), ('P', 'Programacion')], max_length=20)),
                ('titulo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliovirtual.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliovirtual.Persona')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliovirtual.Curso')),
            ],
            bases=('bibliovirtual.persona',),
        ),
        migrations.CreateModel(
            name='MateriaDescargable',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliovirtual.Material')),
            ],
            bases=('bibliovirtual.material',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliovirtual.Persona')),
            ],
            bases=('bibliovirtual.persona',),
        ),
        migrations.CreateModel(
            name='LibroEnVenta',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliovirtual.Material')),
                ('descripcion', models.CharField(max_length=200)),
                ('vendedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliovirtual.Alumno')),
            ],
            bases=('bibliovirtual.material',),
        ),
    ]