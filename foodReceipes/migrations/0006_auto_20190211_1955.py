# Generated by Django 2.1.4 on 2019-02-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodReceipes', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='learn_comment',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
