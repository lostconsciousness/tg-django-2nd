# Generated by Django 4.1.7 on 2023-03-13 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podik',
            old_name='piture',
            new_name='picture',
        ),
    ]