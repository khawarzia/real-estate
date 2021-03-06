# Generated by Django 2.2 on 2020-09-11 11:51

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
            name='profileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.BooleanField(default=True)),
                ('Agent_or_Buyer', models.CharField(blank=True, choices=[('Buyer', 'Buyer'), ('Agent', 'Agent')], default='Buyer', max_length=10)),
                ('is_master_agent', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, default='', max_length=11)),
                ('occupation', models.CharField(blank=True, default='', max_length=200)),
                ('minprice', models.CharField(blank=True, default=' ', max_length=200)),
                ('maxprice', models.CharField(blank=True, default=' ', max_length=200)),
                ('minsqft', models.CharField(blank=True, default=' ', max_length=200)),
                ('maxsqft', models.CharField(blank=True, default=' ', max_length=200)),
                ('beds', models.CharField(blank=True, default='1', max_length=200)),
                ('bath', models.CharField(blank=True, default='1', max_length=200)),
                ('minlot', models.CharField(blank=True, default=' ', max_length=200)),
                ('maxlot', models.CharField(blank=True, default=' ', max_length=200)),
                ('stories', models.CharField(blank=True, default=' ', max_length=200)),
                ('any_other', models.CharField(blank=True, default=' ', max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sf', models.BooleanField(default=False)),
                ('th', models.BooleanField(default=False)),
                ('cd', models.BooleanField(default=False)),
                ('mf', models.BooleanField(default=False)),
                ('ln', models.BooleanField(default=False)),
                ('schools', models.BooleanField(default=False)),
                ('commute', models.BooleanField(default=False)),
                ('vastu', models.BooleanField(default=False)),
                ('shop', models.BooleanField(default=False)),
                ('neighbourhood', models.CharField(blank=True, max_length=200)),
                ('pre_approval', models.BooleanField(default=False)),
                ('soon_looking_to_buy', models.CharField(blank=True, max_length=200, null=True)),
                ('selopt', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
