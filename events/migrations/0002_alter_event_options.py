# Generated by Django 3.2.24 on 2024-03-04 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_on']},
        ),
    ]
