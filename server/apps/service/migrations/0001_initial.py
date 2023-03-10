# Generated by Django 4.1.4 on 2022-12-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Service type name', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Service Type',
                'verbose_name_plural': 'Service Types',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Package description', max_length=255, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Package price', max_digits=15, verbose_name='Price')),
                ('service_type', models.ForeignKey(help_text='Package service type', on_delete=django.db.models.deletion.PROTECT, to='service.servicetype', verbose_name='Service type')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Deliverable name', max_length=255, verbose_name='Name')),
                ('package', models.ForeignKey(help_text='Package', on_delete=django.db.models.deletion.PROTECT, to='service.package', verbose_name='Package')),
            ],
            options={
                'verbose_name': 'Deliverable',
                'verbose_name_plural': 'Deliverables',
            },
        ),
    ]
