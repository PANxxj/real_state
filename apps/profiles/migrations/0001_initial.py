# Generated by Django 3.2.23 on 2024-02-03 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+917898756663', max_length=30, region=None, verbose_name='phone number')),
                ('about_me', models.TextField(default='Say something about yourself', verbose_name='About Me ')),
                ('aadhar', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=20)),
                ('country', django_countries.fields.CountryField(default='India', max_length=2)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('is_buyer', models.BooleanField(default=False, help_text='Are Looking for Buy a property', verbose_name='Buyer')),
                ('is_seller', models.BooleanField(default=False, help_text='Are Looking to Sell a property', verbose_name='Seller')),
                ('is_agent', models.BooleanField(default=False, help_text='Are an Agent', verbose_name='Agent')),
                ('top_agent', models.BooleanField(default=False, verbose_name='Top Agent')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of Review ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
