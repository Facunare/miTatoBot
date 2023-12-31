# Generated by Django 4.2.1 on 2023-06-25 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatoApp', '0004_alter_materias_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriasConstrucciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=180)),
                ('descripcion', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='materiasConstImages')),
            ],
        ),
    ]
