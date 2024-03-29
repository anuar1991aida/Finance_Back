# Generated by Django 4.1.2 on 2023-06-17 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dirs', '0005_organization_deleted'),
        ('docs', '0007_izm_inc_tbl1_itog1_izm_inc_tbl1_itog10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='izm_inc_tbl1',
            name='_budjet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.budjet', verbose_name='Бюджет документа'),
        ),
        migrations.CreateModel(
            name='import219_tbl1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_date', models.DateField(null=True)),
                ('deleted', models.BooleanField(default=False, null=True)),
                ('sm1', models.FloatField(null=True)),
                ('sm2', models.FloatField(null=True)),
                ('sm3', models.FloatField(null=True)),
                ('sm4', models.FloatField(null=True)),
                ('sm5', models.FloatField(null=True)),
                ('sm6', models.FloatField(null=True)),
                ('sm7', models.FloatField(null=True)),
                ('sm8', models.FloatField(null=True)),
                ('sm9', models.FloatField(null=True)),
                ('sm10', models.FloatField(null=True)),
                ('_budjet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.budjet', verbose_name='Бюджет документа')),
                ('_classification', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.classification_income', verbose_name='Классификация документа')),
                ('_izm_inc', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='docs.izm_inc', verbose_name='ИД документа')),
                ('_organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.organization', verbose_name='Организация документа')),
            ],
        ),
        migrations.CreateModel(
            name='import219',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(null=True)),
                ('_date', models.DateField(null=True)),
                ('deleted', models.BooleanField(default=False, null=True)),
                ('_budjet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.budjet', verbose_name='Бюджет документа')),
                ('_organization', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.organization', verbose_name='Организация документа')),
            ],
        ),
    ]
