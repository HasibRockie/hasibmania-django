# Generated by Django 3.2.7 on 2022-06-23 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='number',
            new_name='id',
        ),
    ]