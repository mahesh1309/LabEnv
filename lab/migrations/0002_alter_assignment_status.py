# Generated by Django 4.1.3 on 2022-11-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]