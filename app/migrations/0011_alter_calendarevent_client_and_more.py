# Generated by Django 4.2.9 on 2024-05-16 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_calendarevent_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.clientmodel'),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='medecin',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.medecinmodel'),
        ),
    ]