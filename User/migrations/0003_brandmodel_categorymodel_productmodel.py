# Generated by Django 4.2.4 on 2023-09-12 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_slider1model_delete_slidermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('brand_des', models.CharField(max_length=200)),
                ('brand_logo', models.ImageField(upload_to='static/logo')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('categoty_des', models.TextField()),
                ('category_logo', models.ImageField(upload_to='satic/logo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.IntegerField()),
                ('product_dis', models.TextField()),
                ('product_Warranty', models.CharField(max_length=200)),
                ('category_color', models.CharField(max_length=300)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.brandmodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.categorymodel')),
            ],
        ),
    ]
