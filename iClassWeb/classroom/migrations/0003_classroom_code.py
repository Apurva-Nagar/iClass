# Generated by Django 3.0.1 on 2019-12-30 10:39

from __future__ import unicode_literals
from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    Classroom = apps.get_model('classroom', 'Classroom')
    for row in Classroom.objects.all():
        row.uuid = uuid.uuid4()
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20191230_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.UUIDField(unique=True),
        )
    ]
