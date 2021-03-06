# Generated by Django 3.2.2 on 2021-05-11 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChainLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='stat',
            old_name='id_pokemon',
            new_name='pokemon',
        ),
        migrations.RemoveField(
            model_name='evolutionchain',
            name='evolution_1',
        ),
        migrations.RemoveField(
            model_name='evolutionchain',
            name='evolution_2',
        ),
        migrations.RemoveField(
            model_name='evolutionchain',
            name='evolution_3',
        ),
        migrations.RemoveField(
            model_name='evolutionchain',
            name='id_api',
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('evolution_chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.evolutionchain')),
            ],
        ),
        migrations.CreateModel(
            name='EvolvesTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chainlink')),
            ],
        ),
        migrations.AddField(
            model_name='chainlink',
            name='evolves_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.evolvesto'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.specie'),
        ),
        migrations.AddField(
            model_name='evolutionchain',
            name='chain_link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.chainlink'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='specie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.specie'),
            preserve_default=False,
        ),
    ]
