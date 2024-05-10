# Generated by Django 5.0.2 on 2024-04-25 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_verify_image'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admmin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='rate1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='rate2',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='rate3',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='rate4',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='rate5',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='verify_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nid',
            field=models.CharField(default=300080424064558, max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='الرقم القومي لابد ان يكون 14 رقم ', regex='^\\d{14}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
