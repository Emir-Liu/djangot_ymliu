from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):

    def __str__(self):
        return self.name

    STATUS_NORMAL = 1
    STATUS_DELETE = 0

    STATUS_ITEM = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')

    status = models.PositiveIntegerField(
        default=STATUS_NORMAL,
        choices=STATUS_ITEM,
        verbose_name='状态'
    )

    is_nav = models.BooleanField(
        default=False,
        verbose_name='是否为导航'
    )

    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )

    class Meta:
        verbose_name = verbose_name_plural = '分类'

class Tag(models.Model):

    def __str__(self):
        return self.name

    STATUS_NORMAL = 1
    STATUS_DELETE = 0

    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name='状态')

    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )

    class Meta:
        verbose_name = verbose_name_plural = '标签'

class Post(models.Model):

    def __str__(self):
        return self.title

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2

    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=255, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须为Markdown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')

    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    owner = models.ForeignKey(
        User,
        verbose_name='作者',
        on_delete=models.CASCADE
    )

    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

