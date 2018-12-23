# Generated by Django 2.1.4 on 2018-12-23 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_url', models.URLField(max_length=2000)),
                ('shortened_url', models.URLField()),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
