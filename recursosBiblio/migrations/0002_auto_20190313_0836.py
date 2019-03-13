# Generated by Django 2.1.7 on 2019-03-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursosBiblio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('DNI', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nom', models.TextField()),
                ('cognom', models.TextField()),
                ('nacionalidad', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id_biblio', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nom', models.TextField()),
                ('ciutat', models.TextField()),
                ('codi_postal', models.TextField()),
                ('carrer', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='escrit_per', to='recursosBiblio.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='biblioteca',
            field=models.ManyToManyField(to='recursosBiblio.Biblioteca'),
        ),
    ]
