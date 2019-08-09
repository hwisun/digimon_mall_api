# Generated by Django 2.2.4 on 2019-08-09 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kinds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField(null=True)),
                ('desc', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('attri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to='monster.Attribute')),
                ('gener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to='monster.Generation')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to='monster.Kinds')),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='uploads/monster_images/')),
            ],
        ),
        migrations.CreateModel(
            name='UserMonster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('tiems', models.DateTimeField(auto_now_add=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monster.List')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='monster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to='monster.Monster'),
        ),
        migrations.AddField(
            model_name='list',
            name='prev',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='monster.Monster'),
        ),
    ]
