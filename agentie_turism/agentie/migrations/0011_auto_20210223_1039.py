# Generated by Django 3.1.6 on 2021-02-23 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentie', '0010_auto_20210223_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Email',
            field=models.EmailField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Responsabil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agentie.responsabil'),
        ),
    ]
