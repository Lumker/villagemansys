# Generated by Django 4.2.3 on 2023-07-29 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resident',
            name='address',
        ),
        migrations.AddField(
            model_name='household',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
