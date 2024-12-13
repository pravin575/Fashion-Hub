# Generated by Django 5.1.3 on 2024-12-11 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=20)),
                ('full_name', models.CharField(max_length=900)),
                ('email', models.EmailField(max_length=900)),
                ('shipping_address', models.TextField(max_length=20000)),
                ('amount_paid', models.IntegerField(default=0)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('shipped', models.BooleanField(default=False)),
                ('date_shipped', models.DateTimeField(blank=True, null=True)),
                ('placed', models.BooleanField(default=False)),
                ('emailsend', models.BooleanField(default=False)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
