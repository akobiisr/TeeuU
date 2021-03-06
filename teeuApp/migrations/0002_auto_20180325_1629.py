# Generated by Django 2.0.1 on 2018-03-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teeuApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, verbose_name='Titre')),
                ('predicateur', models.CharField(max_length=50, verbose_name='Predicateur')),
                ('date_pred', models.DateTimeField(verbose_name='Date de la predication')),
                ('date_enreg', models.DateTimeField(auto_now_add=True, verbose_name='Date de Publication')),
                ('date_modif', models.DateTimeField(auto_now=True, verbose_name='Date de derniere Modification')),
                ('genre', models.CharField(choices=[('video', 'Video'), ('Audio', 'Audio'), ('Text', 'Text')], max_length=10, verbose_name='Genre')),
                ('predication', models.FileField(max_length=200, upload_to='video')),
            ],
        ),
        migrations.DeleteModel(
            name='Media_Enseignement',
        ),
    ]
