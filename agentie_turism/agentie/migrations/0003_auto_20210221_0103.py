# Generated by Django 3.1.6 on 2021-02-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentie', '0002_auto_20210217_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pachet_turistic',
            name='Client',
            field=models.ManyToManyField(blank=True, to='agentie.Client'),
        ),
        migrations.AlterField(
            model_name='pachet_turistic',
            name='Zi_inceput',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Plecare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nume_locatie', models.CharField(max_length=30)),
                ('Destinatie', models.ManyToManyField(blank=True, to='agentie.Destinatie')),
            ],
        ),
    ]
