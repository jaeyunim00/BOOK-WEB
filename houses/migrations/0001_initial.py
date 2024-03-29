# Generated by Django 4.2.5 on 2023-09-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('price', models.PositiveBigIntegerField()),
                ('description', models.TextField()),
                ('isBooked', models.BooleanField()),
                ('address', models.CharField(max_length=140)),
            ],
        ),
    ]
