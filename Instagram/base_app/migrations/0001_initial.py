# Generated by Django 2.0.6 on 2018-07-09 14:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
                ('likes', models.PositiveIntegerField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.User'),
        ),
        migrations.AddField(
            model_name='like',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Picture'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Picture'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.User'),
        ),
    ]
