# Generated by Django 2.1.7 on 2019-04-06 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techquiz', '0002_auto_20190320_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.CharField(max_length=3)),
                ('Play_date', models.CharField(max_length=10)),
                ('Quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techquiz.quiz')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Birth_Date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='managescore',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techquiz.user'),
        ),
    ]
