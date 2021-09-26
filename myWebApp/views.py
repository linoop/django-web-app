from django.shortcuts import render
from myWebApp.models import Question
from account.models import Account
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from operator import attrgetter
from blog.views import get_blog_queryset

BLOG_POSTS_PER_PAGE = 10


def homeScreenView(request):
    # print(request.headers)
    context = {}
    # context['first'] = 'item1'
    # context['second'] = 'item2'
    # or
    # context = {'some_string': 'This is some string', 'some_number': 'This is number'}

    # list_of_values = ['item1', 'item2', 'item3']
    # list_of_values = []
    # list_of_values.append('item1')
    # list_of_values.append('item2')
    # list_of_values.append('item3')
    # context['list_of_values'] = list_of_values

    # questions = Question.objects.all()
    # context['questions'] = questions
    # context['accounts'] = Account.objects.all()

    # Search
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)

