# Generated by Django 2.2.6 on 2019-12-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(blank=True, max_length=10, null=True)),
                ('course_title', models.CharField(blank=True, max_length=200, null=True)),
                ('course_credit', models.IntegerField(default=0)),
                ('elective', models.BooleanField(default=False)),
            ],
        ),
    ]
