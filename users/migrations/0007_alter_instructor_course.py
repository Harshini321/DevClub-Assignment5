# Generated by Django 4.0.6 on 2022-07-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='course',
            field=models.CharField(max_length=6),
        ),
    ]
