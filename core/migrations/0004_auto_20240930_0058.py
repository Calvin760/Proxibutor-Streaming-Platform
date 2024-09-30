# Generated by Django 2.1 on 2024-09-29 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240923_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=255)),
                ('header_image', models.ImageField(upload_to='artist_headers/')),
                ('profile_picture', models.ImageField(upload_to='artist_profiles/')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='music',
            name='stage_name',
        ),
        migrations.AddField(
            model_name='music',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Artist'),
        ),
    ]
