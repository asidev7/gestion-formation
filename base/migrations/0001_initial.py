# Generated by Django 5.0.2 on 2024-02-28 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Instructeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('prix', models.PositiveBigIntegerField()),
                ('lieu', models.CharField(max_length=255, verbose_name='Lieu')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.categorie', verbose_name='Catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.client')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.formation')),
            ],
        ),
        migrations.AddField(
            model_name='formation',
            name='participants',
            field=models.ManyToManyField(through='base.Inscription', to='base.client', verbose_name='Participants'),
        ),
        migrations.AddField(
            model_name='formation',
            name='instructeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.instructeur', verbose_name='Instructeur'),
        ),
        migrations.AddField(
            model_name='formation',
            name='personnel',
            field=models.ManyToManyField(to='base.personnel', verbose_name='Personnel'),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(verbose_name='Date de début')),
                ('date_fin', models.DateField(verbose_name='Date de fin')),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('lieu', models.CharField(max_length=255, verbose_name='Lieu')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='base.formation')),
            ],
        ),
        migrations.AddField(
            model_name='instructeur',
            name='specialites',
            field=models.ManyToManyField(to='base.specialite', verbose_name='Spécialités'),
        ),
    ]
