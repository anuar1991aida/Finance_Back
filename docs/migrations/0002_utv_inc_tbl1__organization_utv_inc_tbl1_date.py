# Generated by Django 4.1.2 on 2023-06-09 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dirs', '0003_rename_category_classification_income__category_and_more'),
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utv_inc_tbl1',
            name='_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.organization', verbose_name='Организация документа'),
        ),
        migrations.AddField(
            model_name='utv_inc_tbl1',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
