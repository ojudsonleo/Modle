# Generated by Django 3.2.4 on 2021-06-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_alter_message_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='alert',
            field=models.CharField(blank=True, default='message whas sended', max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
