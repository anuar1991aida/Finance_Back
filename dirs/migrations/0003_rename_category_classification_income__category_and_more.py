# Generated by Django 4.1.2 on 2023-06-09 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dirs', '0002_budjet_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classification_income',
            old_name='category',
            new_name='_category',
        ),
        migrations.RenameField(
            model_name='classification_income',
            old_name='classs',
            new_name='_classs',
        ),
        migrations.RenameField(
            model_name='classification_income',
            old_name='podclass',
            new_name='_podclass',
        ),
        migrations.RenameField(
            model_name='classification_income',
            old_name='spec',
            new_name='_spec',
        ),
    ]
