# Generated by Django 3.2.8 on 2021-11-25 06:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_metadata', '0266_auto_20210624_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnerPathwayProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LearnerPathwayCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course_metadata.course')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='learner_pathway.learnerpathwayprogram')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
