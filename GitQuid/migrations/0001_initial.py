# Generated by Django 2.0.3 on 2018-03-14 17:05

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
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField()),
                ('comment', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('media', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField(null=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.BinaryField(null=True)),
                ('description', models.TextField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GitQuid.UserProfile'),
        ),
        migrations.AddField(
            model_name='media',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GitQuid.Project'),
        ),
        migrations.AddField(
            model_name='donation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GitQuid.Project'),
        ),
        migrations.AddField(
            model_name='donation',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GitQuid.UserProfile'),
        ),
    ]
