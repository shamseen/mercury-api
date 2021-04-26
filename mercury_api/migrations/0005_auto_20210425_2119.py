# Generated by Django 3.2 on 2021-04-26 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mercury_api', '0004_rename_runner_id_result_runner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='cohort_id',
            new_name='cohort',
        ),
        migrations.RemoveField(
            model_name='result',
            name='race_year',
        ),
        migrations.AddField(
            model_name='result',
            name='race',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.RESTRICT, related_name='results', to='mercury_api.race'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.RemoveField(
            model_name='result',
            name='runner',
        ),
        migrations.AddField(
            model_name='result',
            name='runner',
            field=models.ManyToManyField(to='mercury_api.Runner'),
        ),
    ]
