# Generated by Django 4.0.3 on 2022-04-05 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_remove_bot_reg_id_alter_bot_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='id',
            new_name='reg_id',
        ),
    ]
