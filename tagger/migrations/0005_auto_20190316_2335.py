# Generated by Django 2.1.7 on 2019-03-16 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0004_auto_20190316_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
