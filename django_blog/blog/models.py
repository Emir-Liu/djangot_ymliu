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

    @classmethod
    def get_navs(cls):
        '''
        根据Category,获取导航和Category

        Returns:

        '''
        categories = cls.objects.filter(status = cls.STATUS_NORMAL)

        nav_categories = []
        normal_categories = []

        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)

        return {
            'navs': nav_categories,
            'categories': normal_categories
        }

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
    '''
    文章对应的模型
    '''

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

    pv = models.PositiveIntegerField(
        default=1
    )

    uv = models.PositiveIntegerField(
        default=1
    )

    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status = cls.STATUS_NORMAL)

    @staticmethod
    def get_by_tag(tag_id):
        '''
        通过tag，查询数据

        Args:
            tag_id:

        Returns:

        '''

        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status = Post.STATUS_NORMAL).select_related('owner', 'category')

        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        '''
        通过Category查询数据

        Args:
            category_id:

        Returns:

        '''
        try:
            category = Category.objects.get(id=category_id)
        except category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(category_id=category_id).select_related('owner', 'category')

        return post_list, category

    @classmethod
    def latest_posts(cls):
        '''
        查询最新的数据

        Returns:

        '''
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)
        return queryset


