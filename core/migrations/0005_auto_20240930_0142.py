# Generated by Django 2.1 on 2024-09-29 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240930_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Artist'),
        ),
        migrations.RemoveField(
            model_name='music',
            name='id_user',
        ),
        migrations.AlterUniqueTogether(
            name='music',
            unique_together={('title', 'artist')},
        ),
    ]
