# Generated by Django 3.0.3 on 2020-04-28 09:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('CurriculumID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('CurriculumName', models.CharField(max_length=50)),
                ('FacultyName', models.CharField(choices=[('FAH', 'Arts And Humanities'), ('FBA', 'Business Admin'), ('FEd', 'Education'), ('FRS', 'Religous Studies'), ('FOS', 'Science'), ('FIT', 'Information Technology'), ('FON', 'Nursing')], max_length=50)),
                ('CreateDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='CourseOutline',
            fields=[
                ('CourseOutlineID', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=99)),
                ('CourseCode', models.CharField(max_length=8)),
                ('FacultyName', models.CharField(choices=[('FAH', 'Arts And Humanities'), ('FBA', 'Business Admin'), ('FEd', 'Education'), ('FRS', 'Religous Studies'), ('FOS', 'Science'), ('FIT', 'Information Technology'), ('FON', 'Nursing')], max_length=50)),
                ('CreateDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('CourseCurriculumID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courseoutline.Curriculum')),
            ],
        ),
    ]
