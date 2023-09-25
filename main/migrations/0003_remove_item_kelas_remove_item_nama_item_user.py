# Generated by Django 4.2.5 on 2023-09-25 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_rename_product_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='kelas',
        ),
        migrations.RemoveField(
            model_name='item',
            name='nama',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]