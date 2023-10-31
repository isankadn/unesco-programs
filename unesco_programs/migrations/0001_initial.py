# Generated by Django 3.2.16 on 2023-10-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0005_auto_20221228_0249'),
        ('course_overviews', '0026_courseoverview_entrance_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnescoProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Name of the program', max_length=255, null=True)),
                ('description', models.TextField(blank=True, default=None, help_text='Description of the program', max_length=500, null=True)),
                ('banner_image', models.ImageField(upload_to='program_banners/')),
                ('courses', models.ManyToManyField(blank=True, db_table='unesco_programs_program_courses', help_text='Courses that are part of the program', related_name='unesco_programs', related_query_name='unesco_program', to='course_overviews.CourseOverview')),
                ('organizations', models.ManyToManyField(blank=True, help_text='Organizations under which the program is allowed', to='organizations.Organization')),
            ],
        ),
    ]
