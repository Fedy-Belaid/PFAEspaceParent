# Generated by Django 3.1.7 on 2021-05-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matière', models.CharField(max_length=10, null=True)),
                ('Note', models.PositiveIntegerField(null=True)),
                ('Coefficient', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]