# Generated by Django 2.1.7 on 2019-03-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0003_auto_20190316_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conv_id', models.CharField(max_length=10)),
                ('turn_id', models.CharField(max_length=3)),
                ('conv_cat', models.CharField(max_length=200)),
                ('speaker', models.CharField(max_length=5)),
                ('text', models.CharField(max_length=300)),
                ('intent', models.CharField(max_length=100, null=True)),
                ('ner', models.CharField(max_length=100, null=True)),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='ReadConv',
        ),
    ]
