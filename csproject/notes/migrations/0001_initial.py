# Generated by Django 3.1.2 on 2020-12-22 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.owner')),
            ],
        ),
    ]