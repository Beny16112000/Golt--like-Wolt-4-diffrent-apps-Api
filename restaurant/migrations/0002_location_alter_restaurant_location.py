# Generated by Django 4.1.5 on 2023-01-19 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=90)),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.location'),
        ),
    ]