# Generated by Django 3.2.3 on 2021-06-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfollio', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='\\media'),
        ),
    ]
