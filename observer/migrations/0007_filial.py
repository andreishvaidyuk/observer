# Generated by Django 2.1.1 on 2018-09-12 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('observer', '0006_auto_20180912_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a filial name', max_length=20)),
                ('phone', models.CharField(help_text='Enter Phone of Filial', max_length=20)),
                ('address', models.CharField(help_text='Enter Address of Filial', max_length=20)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
