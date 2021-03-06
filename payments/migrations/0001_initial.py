# Generated by Django 2.1.1 on 2019-04-29 12:40

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('amount_paid', models.FloatField(blank=True)),
                ('description', models.CharField(max_length=255)),
                ('payment_date', models.DateField(auto_now=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('invoice_no', models.CharField(blank=True, max_length=255)),
                ('house', models.ForeignKey(on_delete='CASCADE', related_name='invoices', to='houses.House')),
                ('tenant', models.ForeignKey(on_delete='CASCADE', related_name='tenant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
