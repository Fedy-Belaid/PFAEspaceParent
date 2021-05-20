# Generated by Django 3.1.7 on 2021-05-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='Class',
            field=models.CharField(choices=[('1ère année', '1ère année'), ('2ème année Sciences Exp', '2ème année Sciences Exp'), ('2ème année Lettres', '2ème année Lettres'), ('2ème année Eco & Gestion', '2ème année Eco & Gestion'), ('2ème année Informatique', '2ème année Informatique'), ('3ème année Sciences', '3ème année Sciences'), ('3ème année Lettres', '3ème année Lettres'), ('3ème année Eco & Gestion', '3ème année Eco & Gestion'), ('3ème année Informatique', '3ème année Informatique'), ('4ème année Sciences', '4ème année Sciences'), ('4ème année Lettres', '4ème année Lettres'), ('4ème année Eco & Gestion', '4ème année Eco & Gestion'), ('4ème année Informatique', '4ème année Informatique')], default='1ère année', max_length=30),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('1ère année', '1ère année'), ('2ème année Sciences Exp', '2ème année Sciences Exp'), ('2ème année Lettres', '2ème année Lettres'), ('2ème année Eco & Gestion', '2ème année Eco & Gestion'), ('2ème année Informatique', '2ème année Informatique'), ('3ème année Sciences', '3ème année Sciences'), ('3ème année Lettres', '3ème année Lettres'), ('3ème année Eco & Gestion', '3ème année Eco & Gestion'), ('3ème année Informatique', '3ème année Informatique'), ('4ème année Sciences', '4ème année Sciences'), ('4ème année Lettres', '4ème année Lettres'), ('4ème année Eco & Gestion', '4ème année Eco & Gestion'), ('4ème année Informatique', '4ème année Informatique')], default='1ère année', max_length=30),
        ),
    ]