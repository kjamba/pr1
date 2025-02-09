# Generated by Django 3.0.1 on 2020-05-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата попадания в справчник')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('schedule', models.TextField(null=True, verbose_name='График работы')),
                ('owner', models.CharField(max_length=50, null=True, verbose_name='Владелец')),
                ('contacts', models.TextField(null=True, verbose_name='Контакты')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='Адрес')),
                ('active', models.BooleanField(default=True, verbose_name='Организация активна')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
