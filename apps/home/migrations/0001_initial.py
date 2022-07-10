# Generated by Django 4.0.6 on 2022-07-10 12:11

import autoslug.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/category/', verbose_name='Kategori Fotosu:')),
                ('name', models.CharField(max_length=20, verbose_name='Kategori')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yayınlama Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategori',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Başlık')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon')),
                ('address', models.TextField(verbose_name='Adres')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yayınlama Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişim',
                'db_table': 'contact',
                'ordering': ['publish'],
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/cover/', verbose_name='Anasayfa Kapak')),
                ('title', models.CharField(help_text='Anasayfa', max_length=20, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='İçerik')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yayınlama Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Kapak',
                'verbose_name_plural': 'Kapak',
                'db_table': 'cover',
                'ordering': ['publish'],
            },
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Ad Soyad:')),
                ('email', models.EmailField(max_length=254, verbose_name='Email:')),
                ('topic', models.CharField(max_length=50, verbose_name='Konu:')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon')),
                ('message', models.TextField(verbose_name='Mesaj')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Gönderilme Tarihi')),
            ],
            options={
                'verbose_name': 'Site Ayarları',
                'verbose_name_plural': 'Site Ayarları',
                'db_table': 'inbox',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Site Adı')),
                ('type', models.CharField(max_length=20, verbose_name='Site Türü')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yayınlama Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Site Başlığı',
                'verbose_name_plural': 'Site Başlığı',
                'db_table': 'title',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='posts/', verbose_name='Gönderi Fotosu:')),
                ('title', models.CharField(max_length=250, verbose_name='Başlık:')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='İçerik')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yayınlama Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('status', models.CharField(choices=[('DF', 'Taslak'), ('PB', 'Yayınla')], default='DF', max_length=2, verbose_name='Yayınlanma Durumu')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gönderi', to='Anasayfa.category', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Gönderi',
                'verbose_name_plural': 'Gönderi',
                'db_table': 'posts',
                'ordering': ['publish'],
            },
        ),
        migrations.AddIndex(
            model_name='posts',
            index=models.Index(fields=['publish'], name='posts_publish_cbdb19_idx'),
        ),
    ]
