# Generated by Django 2.2.4 on 2021-02-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='vypiska_fle',
            new_name='vypiska_file',
        ),
        migrations.AlterField(
            model_name='lead',
            name='driverLicense',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
