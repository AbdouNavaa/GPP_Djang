# Generated by Django 5.0.7 on 2024-08-05 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='TC', max_length=3, unique=True)),
                ('description', models.CharField(default='', max_length=50)),
                ('semestres', models.CharField(choices=[('1,2', '1,2'), ('3,6', '3,6')], default='1,2', max_length=4)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=6)),
                ('cred', models.IntegerField(default=2)),
                ('semestre', models.IntegerField()),
                ('nombre_heures', models.IntegerField(default=24)),
                ('group_cm', models.TextField(default='')),
                ('group_tp', models.TextField(default='')),
                ('group_td', models.TextField(default='')),
                ('prix', models.FloatField(default=500)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPP.filiere')),
                ('prof_cm', models.ManyToManyField(related_name='matiere_cm', to='account.prof')),
                ('prof_td', models.ManyToManyField(related_name='matiere_td', to='account.prof')),
                ('prof_tp', models.ManyToManyField(related_name='matiere_tp', to='account.prof')),
            ],
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CM', 'CM'), ('TP', 'TP'), ('TD', 'TD')], max_length=2)),
                ('nbh', models.FloatField(default=0)),
                ('deb', models.TimeField()),
                ('groupe', models.CharField(default='G', max_length=10)),
                ('fin', models.TimeField()),
                ('jour', models.CharField(choices=[('Dimanche', 'Dimanche'), ('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi')], max_length=10)),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.prof')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPP.filiere')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPP.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe', models.CharField(default='G', max_length=10)),
                ('type', models.CharField(choices=[('CM', 'CM'), ('TP', 'TP'), ('TD', 'TD')], max_length=2)),
                ('nbh', models.FloatField(default=0)),
                ('date_creation', models.DateTimeField()),
                ('deb', models.TimeField()),
                ('fin', models.TimeField()),
                ('taux', models.FloatField(default=0)),
                ('isSigned', models.CharField(choices=[('effectué', 'effectué'), ('en attente', 'en attente'), ('annulé', 'annulé')], default='en attente', max_length=10)),
                ('isPaid', models.CharField(choices=[('en attente', 'en attente'), ('préparé', 'préparé'), ('effectué', 'effectué')], default='en attente', max_length=10)),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.prof')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPP.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbh', models.FloatField(default=0)),
                ('nbc', models.FloatField(default=0)),
                ('th', models.FloatField(default=0)),
                ('date_creation', models.DateTimeField()),
                ('fromDate', models.DateTimeField()),
                ('toDate', models.DateTimeField()),
                ('taux', models.FloatField(default=0)),
                ('confirmation', models.CharField(choices=[('en attente', 'en attente'), ('accepté', 'accepté'), ('refusé', 'refusé')], max_length=10)),
                ('message', models.CharField(default='ok', max_length=50)),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.prof')),
            ],
        ),
    ]