# Generated by Django 4.1.3 on 2022-11-15 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_rename_secondary_abilty_super_secondary_ability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='type',
        ),
    ]
