# Generated by Django 4.0 on 2021-12-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_category_alter_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]