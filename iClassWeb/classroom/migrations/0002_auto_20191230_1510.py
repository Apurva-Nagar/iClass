# Generated by Django 3.0.1 on 2019-12-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='room_no',
            field=models.IntegerField(),
        ),
    ]
