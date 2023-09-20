# Generated by Django 4.2.5 on 2023-09-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_learner_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='courses',
            field=models.ManyToManyField(default=[], related_name='learners', to='api.course'),
        ),
    ]