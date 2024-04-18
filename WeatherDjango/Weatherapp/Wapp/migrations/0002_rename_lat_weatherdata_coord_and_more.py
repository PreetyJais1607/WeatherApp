# Generated by Django 5.0.2 on 2024-02-26 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='lat',
            new_name='coord',
        ),
        migrations.RenameField(
            model_name='weatherdata',
            old_name='lon',
            new_name='temp',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='visibility',
        ),
    ]
