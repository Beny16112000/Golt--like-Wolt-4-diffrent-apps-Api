# Generated by Django 4.1.5 on 2023-01-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_delete_dishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('img', models.ImageField(upload_to='media/dishes_images')),
                ('detail', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'verbose_name_plural': 'Dishes',
            },
        ),
    ]
