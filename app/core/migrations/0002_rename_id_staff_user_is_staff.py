# Generated by Django 3.2.25 on 2024-04-12 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_staff',
            new_name='is_staff',
        ),
    ]
