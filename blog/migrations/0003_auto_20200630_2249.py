# Generated by Django 3.0.7 on 2020-06-30 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200630_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment_id', to='blog.Comment'),
        ),
    ]
