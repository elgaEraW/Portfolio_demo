# Generated by Django 3.1.3 on 2020-12-26 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201226_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribenewsletter',
            options={},
        ),
        migrations.RenameField(
            model_name='subscribenewsletter',
            old_name='email',
            new_name='subscriberemail',
        ),
    ]
