# Generated by Django 3.0.4 on 2020-05-13 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200512_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Trip')),
            ],
        ),
    ]
