# Generated by Django 4.2.3 on 2023-09-03 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ref_number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijk1234567890', length=10, max_length=10, prefix='', unique=True),
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='default.jpg', upload_to='kyc')),
                ('gender', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')], max_length=40)),
                ('date_of_birth', models.DateTimeField()),
                ('signature', models.ImageField(upload_to='kyc')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]