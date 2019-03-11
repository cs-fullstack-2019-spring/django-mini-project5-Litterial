# Generated by Django 2.0.6 on 2019-03-11 18:33

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
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.CharField(max_length=200)),
                ('userTableForeignKey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=200)),
                ('meal_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('date_created', models.DateField()),
                ('creator', models.CharField(max_length=200)),
                ('keytoNewUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipeApp.NewUser')),
            ],
        ),
    ]
