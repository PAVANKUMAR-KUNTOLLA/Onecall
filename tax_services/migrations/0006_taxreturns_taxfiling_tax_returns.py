# Generated by Django 4.2.3 on 2023-11-18 07:30

from django.db import migrations, models
import django.db.models.deletion
import tax_services.models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_services', '0005_bank_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxReturns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(blank=True, null=True, upload_to=tax_services.models.get_tax_returns_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('filing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tax_services.taxfiling')),
            ],
            options={
                'verbose_name': 'Tax Returns',
            },
        ),
        migrations.AddField(
            model_name='taxfiling',
            name='tax_returns',
            field=models.ManyToManyField(to='tax_services.taxreturns'),
        ),
    ]