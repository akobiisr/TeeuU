# Generated by Django 2.0.1 on 2018-04-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teeuApp', '0011_pain_quotidien'),
    ]

    operations = [
        migrations.AddField(
            model_name='pain_quotidien',
            name='nom',
            field=models.CharField(default='Blaise', max_length=100, verbose_name='Nom du posteur'),
            preserve_default=False,
        ),
    ]
