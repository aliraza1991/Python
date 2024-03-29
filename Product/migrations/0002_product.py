# Generated by Django 2.2.3 on 2019-09-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('delivery', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
