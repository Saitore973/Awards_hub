# Generated by Django 4.0.4 on 2022-04-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_project_options_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(max_length=222),
        ),
    ]