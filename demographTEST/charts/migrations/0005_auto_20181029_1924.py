# Generated by Django 2.1.1 on 2018-10-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_education_income'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='college_plus',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='hs',
            new_name='income',
        ),
        migrations.RemoveField(
            model_name='education',
            name='no_hs',
        ),
        migrations.RemoveField(
            model_name='education',
            name='some_college',
        ),
        migrations.AddField(
            model_name='education',
            name='education_level',
            field=models.IntegerField(default=0),
        ),
    ]
