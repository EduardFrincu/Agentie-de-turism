# Generated by Django 3.1.6 on 2021-02-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentie', '0009_auto_20210223_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Telefon',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
