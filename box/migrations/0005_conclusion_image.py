# Generated by Django 3.0.3 on 2020-02-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0004_auto_20200206_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='conclusion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/conc/'),
        ),
    ]
