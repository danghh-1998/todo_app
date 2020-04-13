# Generated by Django 3.0.4 on 2020-04-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('expired_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_token',
            },
        ),
    ]
