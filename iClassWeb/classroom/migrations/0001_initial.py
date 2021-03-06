# Generated by Django 3.0.1 on 2019-12-30 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_customuser_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(max_length=3)),
                ('course', models.CharField(max_length=200)),
                ('student', models.ManyToManyField(to='accounts.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher')),
            ],
        ),
    ]
