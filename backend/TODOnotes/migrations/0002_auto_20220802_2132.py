# Generated by Django 3.2.14 on 2022-08-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOnotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Moderator',
        ),
    ]