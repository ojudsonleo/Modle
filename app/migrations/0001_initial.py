# Generated by Django 3.2.4 on 2021-06-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('langvage', models.CharField(max_length=200)),
            ],
        ),
    ]
