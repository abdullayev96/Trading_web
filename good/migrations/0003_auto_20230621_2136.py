# Generated by Django 3.2.4 on 2023-06-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_auto_20230617_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchi',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='helper',
            options={'ordering': ['id'], 'verbose_name': 'Manzil', 'verbose_name_plural': 'Manzillar'},
        ),
    ]
