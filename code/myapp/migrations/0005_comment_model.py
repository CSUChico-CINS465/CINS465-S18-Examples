# Generated by Django 2.0.1 on 2018-03-15 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180227_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=240)),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Suggestion_Model')),
            ],
        ),
    ]
