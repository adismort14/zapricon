# Generated by Django 4.1.3 on 2022-11-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messName', models.CharField(max_length=255)),
                ('complaint', models.TextField()),
            ],
        ),
    ]
