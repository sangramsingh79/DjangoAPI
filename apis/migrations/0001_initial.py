# Generated by Django 4.2.4 on 2024-07-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=2)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
    ]
