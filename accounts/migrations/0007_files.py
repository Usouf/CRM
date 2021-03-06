# Generated by Django 3.1.3 on 2020-11-29 13:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201129_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='documents', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]
