# Generated by Django 3.0.3 on 2020-02-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.TextField(),
        ),
    ]
