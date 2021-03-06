# Generated by Django 2.0.1 on 2018-05-11 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teeuApp', '0012_pain_quotidien_nom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire_pain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Commentaire', models.TextField(verbose_name='Commentaire')),
                ('id_pain', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teeuApp.Pain_Quotidien')),
            ],
        ),
        migrations.CreateModel(
            name='Reply_pain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='Reply')),
                ('id_comment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teeuApp.Commentaire_pain')),
            ],
        ),
    ]
