# Generated by Django 4.0.4 on 2022-06-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compte', '0003_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='exemple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(blank=True, db_column='A', max_length=34, null=True)),
                ('b', models.CharField(blank=True, db_column='B', max_length=10, null=True)),
                ('c', models.CharField(blank=True, db_column='C', max_length=10, null=True)),
                ('d', models.CharField(blank=True, db_column='D', max_length=10, null=True)),
                ('e', models.CharField(blank=True, db_column='E', max_length=8, null=True)),
                ('f', models.CharField(blank=True, db_column='F', max_length=10, null=True)),
                ('g', models.CharField(blank=True, db_column='G', max_length=10, null=True)),
                ('h', models.CharField(blank=True, db_column='H', max_length=13, null=True)),
                ('i', models.CharField(blank=True, db_column='I', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'exemple',
                'verbose_name_plural': 'exemple',
            },
        ),
    ]
