# Generated by Django 2.0.6 on 2018-06-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Goods name', max_length=30, unique=True)),
                ('description', models.CharField(blank=True, help_text='Description', max_length=255, null=True)),
            ],
        ),
    ]
