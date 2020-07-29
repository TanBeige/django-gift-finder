# Generated by Django 2.2.8 on 2020-07-29 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_Hobby', models.CharField(max_length=100)),
                ('category_ageRange', models.IntegerField()),
                ('category_priceRange', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giftTimestamp', models.DateTimeField(auto_created=True, auto_now=True)),
                ('link', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('asin', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=500)),
                ('form_input_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.FormInputs')),
            ],
        ),
    ]
