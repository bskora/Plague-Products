# Generated by Django 4.1a1 on 2022-09-20 21:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
