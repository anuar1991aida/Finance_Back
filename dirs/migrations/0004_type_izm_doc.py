# Generated by Django 4.1.2 on 2023-06-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirs', '0003_rename_category_classification_income__category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='type_izm_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
            ],
        ),
    ]
