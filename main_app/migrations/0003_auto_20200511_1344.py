# Generated by Django 3.0.4 on 2020-05-11 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-date']},
        ),
    ]