# Generated by Django 2.0.4 on 2019-01-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dos', '0002_auto_20181230_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vipaudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='音频标题')),
                ('url', models.URLField(blank=True, null=True, verbose_name='音频链接')),
                ('note', models.TextField(blank=True, max_length=1000, null=True, verbose_name='笔记')),
                ('pubtime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dos.Vip', verbose_name='课程名')),
            ],
            options={
                'verbose_name': 'DOS校友福利-音频',
                'verbose_name_plural': 'DOS校友福利-音频',
            },
        ),
    ]
