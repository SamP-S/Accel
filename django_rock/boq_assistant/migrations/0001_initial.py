# Generated by Django 5.1.4 on 2024-12-16 13:23

import boq_assistant.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCFModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed', max_length=255, verbose_name='name')),
                ('notes', models.TextField(default='', verbose_name='notes')),
                ('mc_file', models.FileField(upload_to='', validators=[boq_assistant.models.validate_file_is_csv], verbose_name='maxcut_file')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('warnings', models.TextField(default='', verbose_name='warnings')),
                ('gen_file', models.FileField(upload_to='', verbose_name='generated_file')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='QFModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed', max_length=255, verbose_name='name')),
                ('notes', models.TextField(default='', verbose_name='notes')),
                ('q_file', models.FileField(upload_to='', validators=[boq_assistant.models.validate_file_is_excel], verbose_name='quote_file')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('warnings', models.TextField(default='', verbose_name='warnings')),
                ('gen_file', models.FileField(upload_to='', verbose_name='generated_file')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
