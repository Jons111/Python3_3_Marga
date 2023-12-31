# Generated by Django 4.2.6 on 2023-10-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_rename_projects_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('data', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
