# Generated by Django 3.0.1 on 2020-01-01 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_notes_notes_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_question', models.FileField(upload_to='assignment_question')),
                ('assignment_heading', models.CharField(default='Notes Topic', max_length=200)),
                ('deadline', models.DateTimeField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_answer', models.FileField(upload_to='assignment_answer')),
                ('is_submitted', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Assignment')),
            ],
        ),
    ]
