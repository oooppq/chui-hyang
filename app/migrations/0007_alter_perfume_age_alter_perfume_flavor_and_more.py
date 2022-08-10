# Generated by Django 4.0.6 on 2022-08-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_note_middle_note_top_rename_note_note_base_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='age',
            field=models.CharField(choices=[('20', '20'), ('50 or more', '50 or more'), ('30', '30'), ('10', '10'), ('40', '40')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='flavor',
            field=models.CharField(choices=[('Woody', 'woody'), ('oriental', 'oriental'), ('floral', 'floral'), ('fresh', 'fresh')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='gender',
            field=models.CharField(choices=[('woman', 'woman'), ('man', 'man')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='season',
            field=models.CharField(choices=[('winter', 'winter'), ('summer', 'summer'), ('spring', 'spring'), ('fall', 'fall')], max_length=20, null=True),
        ),
    ]
