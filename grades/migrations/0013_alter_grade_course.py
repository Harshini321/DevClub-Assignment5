# Generated by Django 4.0.6 on 2022-07-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_available', '0001_initial'),
        ('grades', '0012_alter_grade_course_alter_grade_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_available.courses'),
        ),
    ]