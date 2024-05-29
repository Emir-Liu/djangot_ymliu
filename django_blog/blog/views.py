from django.shortcuts import render

from .models import Post, Tag

# from django.http import HttpResponse
# Create your views here.

def post_list(request, category_id=None, tag_id=None):
    # content = f'post list category_id={category_id}, tag_id={tag_id}'.format(
    #     category_id = category_id,
    #     tag_id = tag_id
    # )
    #
    # return HttpResponse(content)


    # return render(
    #     request,
    #     'blog/list.html',
    #     context={
    #         'name': 'post_list'
    #     }
    # )

    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status = Post.STATUS_NORMAL)

    else:
        post_list = Post.objects.filter(Post.STATUS_NORMAL)
        if category_id:
            post_list = post_list.filter(category_id=category_id)

    return render(
        request,
        'blog/list.html',
        context={
            'post_list': post_list
        }
    )

def post_detail(request, post_id):
    # return HttpResponse('detail')
    return render(
        request,
        'blog/detail.html',
        context={
            'name': 'post_detail'
        }
    )

