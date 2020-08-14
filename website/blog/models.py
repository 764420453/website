from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass



class Category(models.Model):
    name=models.CharField(verbose_name='分类',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='博客分类'
        verbose_name_plural=verbose_name


class Tag(models.Model):
    name=models.CharField(verbose_name='标签',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='博客标签'
        verbose_name_plural=verbose_name


class Entry(models.Model):
    title=models.CharField(verbose_name='文章标题',max_length=128)
    author=models.ForeignKey('User',verbose_name='作者',on_delete=models.CASCADE)
    img=models.ImageField(verbose_name='博客配图',upload_to='blog_img',null=True,blank=True)
    body=models.TextField(verbose_name='正文',)
    abstract=models.TextField(verbose_name='摘要',max_length=256,null=True,blank=True)
    visiting=models.PositiveIntegerField(verbose_name='访问量',default=0)
    category=models.ManyToManyField('Category',verbose_name='博客分类')
    tags=models.ManyToManyField("Tag",verbose_name='标签')
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    modifyed_time=models.DateTimeField(verbose_name='修改时间',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created_time']
        verbose_name='博客正文'
        verbose_name_plural=verbose_name














