# Generated by Django 2.0.1 on 2018-05-12 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teeuApp', '0014_commentaire_pain_date_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire_pain',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
