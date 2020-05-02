# Generated by Django 3.0.5 on 2020-04-29 07:11

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('salary', models.PositiveSmallIntegerField()),
                ('total_experience', models.DecimalField(decimal_places=2, max_digits=4)),
                ('skill', models.PositiveSmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('client', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('PL', 'Pipeline'), ('OG', 'On Going'), ('CM', 'Completed')], max_length=5)),
                ('score', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=100)),
                ('experience', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Project2Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p2teams', to='demo.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Project2')),
            ],
        ),
        migrations.AddField(
            model_name='project2',
            name='backend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p2bend_projs', to='demo.Technology'),
        ),
        migrations.AddField(
            model_name='project2',
            name='frontend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p2fend_projs', to='demo.Technology'),
        ),
        migrations.AddField(
            model_name='project2',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p2projects', to='demo.Employee'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('client', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('PL', 'Pipeline'), ('OG', 'On Going'), ('CM', 'Completed')], max_length=5)),
                ('score', models.PositiveSmallIntegerField()),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bend_projs', to='demo.Technology')),
                ('engineer', models.ManyToManyField(to='demo.Employee')),
                ('frontend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fend_projs', to='demo.Technology')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projs', to='demo.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_school', models.CharField(max_length=500)),
                ('sec_score', models.DecimalField(decimal_places=2, max_digits=4)),
                ('srsec_school', models.CharField(max_length=500)),
                ('srsec_score', models.DecimalField(decimal_places=2, max_digits=4)),
                ('grade_school', models.CharField(max_length=500)),
                ('grad_score', models.DecimalField(decimal_places=2, max_digits=4)),
                ('postgrad_school', models.CharField(blank=True, max_length=500, null=True)),
                ('postgrad_score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('phd_school', models.CharField(blank=True, max_length=500, null=True)),
                ('phd_score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('postdr_school', models.CharField(blank=True, max_length=500, null=True)),
                ('postdr_score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='demo.Employee')),
            ],
        ),
    ]
