from django.db import models

# 数据表建模：虚拟人物
class Figure(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=10)
    photo = models.ImageField(verbose_name='头像', upload_to='photo', blank=True, null=True)
    color = models.CharField(verbose_name='颜色', max_length=10)

    class Meta:
        verbose_name = '虚拟人物'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 数据表建模：英语对话
class Dialogue(models.Model):
    courseid = models.IntegerField(verbose_name='课程编号')
    partid = models.IntegerField(verbose_name='小节编号')
    index = models.IntegerField(verbose_name='序号')

    spokesperson = models.ForeignKey(Figure, on_delete=models.CASCADE, verbose_name='发言人')

    lr = models.BooleanField(verbose_name='靠左',default=True)
    content = models.TextField(verbose_name='发言内容', max_length=200)
    translate = models.TextField(verbose_name='翻译', max_length=100)

    class Meta:
        verbose_name = '英语对话'
        verbose_name_plural = verbose_name
        ordering = ['-courseid']

# 数据表建模：单词
class Word(models.Model):
    courseid = models.IntegerField(verbose_name='课程编号')
    partid = models.IntegerField(verbose_name='小节编号')
    word = models.CharField(verbose_name='单词', max_length=20)

    class Meta:
        verbose_name = '单词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.word