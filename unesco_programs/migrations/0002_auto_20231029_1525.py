# Generated by Django 3.2.16 on 2023-10-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco_programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unescoprogram',
            name='slug',
            field=models.SlugField(blank=True, help_text='Auto-generated slug for the program', unique=True),
        ),
        migrations.AlterField(
            model_name='unescoprogram',
            name='name',
            field=models.CharField(default=None, help_text='Name of the program', max_length=255, null=True, unique=True),
        ),
    ]
