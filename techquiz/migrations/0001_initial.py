# Generated by Django 2.1.7 on 2019-03-14 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Question', models.CharField(max_length=500)),
                ('Question_Option_1', models.CharField(max_length=100)),
                ('Question_Option_2', models.CharField(max_length=100)),
                ('Question_Option_3', models.CharField(max_length=100)),
                ('Question_Option_4', models.CharField(max_length=100)),
                ('Question_Answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quiz_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tech_Name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Role', models.CharField(max_length=10)),
                ('User_Email', models.EmailField(max_length=100)),
                ('User_Birth_Date', models.DateTimeField(auto_now_add=True)),
                ('User_Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='tech',
            name='Tech_Adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techquiz.user'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Quiz_Adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techquiz.user'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='Quiz_Tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techquiz.tech'),
        ),
        migrations.AddField(
            model_name='question',
            name='Question_Quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techquiz.quiz'),
        ),
    ]
