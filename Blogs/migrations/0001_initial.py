# Generated by Django 3.1.5 on 2021-01-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('Image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
