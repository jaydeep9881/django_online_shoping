# Generated by Django 4.2.5 on 2023-09-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_rename_category_color_productmodel_product_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_mobile', models.CharField(max_length=30)),
                ('user_address', models.TextField()),
                ('user_email', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
            ],
        ),
    ]