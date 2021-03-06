# Generated by Django 4.0.4 on 2022-05-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=300)),
                ('full_info', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=350)),
                ('visible', models.BooleanField(default=True)),
                ('with_deposit', models.BooleanField(default=True)),
            ],
        ),
    ]
