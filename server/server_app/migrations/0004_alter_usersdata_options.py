# Generated by Django 5.0 on 2024-01-05 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0003_alter_usersdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersdata',
            options={'managed': False},
        ),
    ]
