# Generated by Django 4.1.2 on 2022-10-23 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_coinfo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coinfo',
            options={'managed': False},
        ),
    ]
