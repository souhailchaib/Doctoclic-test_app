# Generated by Django 4.2.9 on 2024-05-15 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_calendarevent_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='client',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.clientmodel'),
        ),
    ]