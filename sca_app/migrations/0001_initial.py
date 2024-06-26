# Generated by Django 5.0.1 on 2024-04-20 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('pic', models.FileField(upload_to='Companies/')),
                ('rating', models.CharField(max_length=50)),
                ('type_of_vehicle', models.CharField(choices=[('Car', 'Car'), ('Bike', 'Bike')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=50)),
                ('pic', models.FileField(upload_to='Userpics/')),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('vehicle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.FileField(upload_to='Booking/')),
                ('created', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sca_app.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sca_app.user')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raitng', models.CharField(default='★★★★★', max_length=10)),
                ('remark', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sca_app.booking')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
