# Generated by Django 4.1.1 on 2022-09-16 18:11

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
                ('auth_token', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=10)),
                ('em', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usernm', models.CharField(max_length=100)),
                ('hostelname', models.CharField(max_length=10)),
                ('roomno', models.CharField(max_length=10)),
                ('mobno', models.CharField(max_length=10)),
            ],
        ),
    ]
