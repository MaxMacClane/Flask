# Generated by Django 4.0.5 on 2022-07-18 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('data_added', models.DateField(auto_now_add=True)),
                ('itemLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
    ]