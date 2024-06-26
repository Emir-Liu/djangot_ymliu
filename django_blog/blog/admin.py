

# Register your models here.

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from django_blog.custom_site import custom_site
from django_blog.base_admin import BaseOwnerAdmin

class PostInline(admin.TabularInline):
    fields = (
        'title',
        'desc',
    )

    extra = 1

    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset

@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):

    form = PostAdminForm

    list_display = [
        'title',
        'category',
        'status',
        'created_time',
        'operator',
    ]

    list_display_links = []

    # list_filter = ['category',]
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category_name']

    actions_on_top = True
    actions_on_bottom = True

    fieldsets = (
        (
            '基础配置',
            {
                'description': '基础配置描述',
                'fields': (
                    ('title', 'category'),
                    'status',
                ),
            }

        ),
        (
            '内容',
            {
                'fields':(
                    'desc',
                    'content',
                ),
            }
        ),
        (
            '额外信息',
            {
                'classes':('collapse',),
                'fields':('tag',),
            }
        )
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

