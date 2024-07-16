# Generated by Django 5.0.6 on 2024-07-12 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameAsignature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('0', 'female'), ('1', 'male')], max_length=1)),
                ('phoneNumber', models.IntegerField()),
                ('emailAddress', models.CharField(max_length=500)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolled',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.asignature')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
        ),
    ]
