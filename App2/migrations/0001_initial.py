# Generated by Django 4.1.2 on 2023-04-12 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='product_title')),
                ('slug', models.SlugField(max_length=55, verbose_name='category_slug')),
                ('description', models.TextField(blank=True, verbose_name='category_description')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='media/category', verbose_name='category_image')),
                ('is_active', models.BooleanField(verbose_name='is_active')),
                ('is_featured', models.BooleanField(verbose_name='is_featured')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Product title')),
                ('slug', models.SlugField(max_length=160, verbose_name='Product slug')),
                ('sku', models.CharField(max_length=255, unique=True, verbose_name='Product ID ')),
                ('detail_description', models.TextField(blank=True, null=True, verbose_name='Detail Description')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Product Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_present', models.BooleanField(null=True, verbose_name='Is present')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('status', models.CharField(choices=[('available', 'available'), ('non_available', 'non_available')], default='available', max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App2.category', verbose_name='Product Categoy')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('userid', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='wish title')),
                ('slug', models.CharField(blank=True, max_length=30, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App2.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Relatedimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='relate')),
                ('products', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App2.product')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='', max_length=255, unique=True, verbose_name='Product ID ')),
                ('phonenumber', models.CharField(default='', max_length=10)),
                ('streetaddress', models.CharField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=10)),
                ('pincode', models.CharField(default='', max_length=10)),
                ('country', models.CharField(blank=True, default='india', max_length=10, verbose_name='country')),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App2.product', verbose_name='product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
