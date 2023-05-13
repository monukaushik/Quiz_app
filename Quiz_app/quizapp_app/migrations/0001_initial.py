# Generated by Django 3.2.12 on 2023-02-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quizapp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=1000)),
                ('opt1', models.CharField(max_length=500)),
                ('opt2', models.CharField(max_length=500)),
                ('opt3', models.CharField(max_length=500)),
                ('opt4', models.CharField(max_length=500)),
                ('ans', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=200)),
                ('question', models.CharField(max_length=1000)),
                ('user_answer', models.CharField(default=False, max_length=500, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
