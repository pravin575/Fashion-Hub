# Generated by Django 5.1.3 on 2024-12-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(default='', upload_to='images')),
                ('product_category', models.CharField(choices=[('Mens', 'Mens'), ('Womens', 'Womens'), ('Kids', 'Kids'), ('Mens Sneakers', 'Mens Sneakers'), ('Womens Sneakers', 'Womens Sneakers')], default='', max_length=50)),
            ],
        ),
    ]
