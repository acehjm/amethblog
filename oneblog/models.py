#-*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from material.frontend import Module


class Category(models.Model):
    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'
        ordering = ['-id']

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ('category', (), {'cg': self.cg})

class Article(models.Model):
    #作者
    author = models.ForeignKey(User)
    #标题
    title = models.CharField(max_length=200)
    #分类
    category = models.ForeignKey(Category)
    # 标签
    tag = models.CharField(max_length=50)
    #创建时间
    created_date = models.DateTimeField(default=timezone.now)
    #修改时间
    published_date = models.DateTimeField(blank=True, null=True)
    #正文
    text = models.TextField()

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    def __unicode__(self) :
        return self.title.encode('utf-8')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-published_date']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

class Comment(models.Model):
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

    post = models.ForeignKey(Article)   #文章标题
    author = models.CharField(max_length=20)  #评论作者
    email = models.EmailField()   #邮箱
    text = models.TextField()   #评论
    time_submitted = models.DateTimeField(default=timezone.now)  #评论时间
    ip = models.IPAddressField()      #ip地址

    def __str__(self):
        return '{0}: {1}'.format(self.author, self.post.title)

class Sample(Module):
    icon = 'mdi-image-compare'


