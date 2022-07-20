# Generated by Django 4.0.5 on 2022-07-19 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0010_club_field_year_alter_student_club_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App2.club'),
        ),
        migrations.AlterField(
            model_name='student',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App2.field'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App2.year'),
        ),
    ]
