# Generated by Django 4.1.3 on 2022-11-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_voter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'ordering': ['-created']},
        ),
    ]