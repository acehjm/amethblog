#-*- encoding: utf-8 -*-
from django.shortcuts import render,render_to_response,RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from oneblog.models import *
from django.db.models import Count
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.syndication.views import Feed
from django.views.generic.dates import MonthArchiveView

def article(request):                #主页文章显示
    posts = Article.objects.all().order_by('-published_date')  #获取全部的Article对象
    paginator = Paginator(posts, 4) #每页显示3个
    page = request.GET.get('page')
    categories = Category.objects.all()
    try :
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)
    return render(request,'home.html', {'posts' : posts, "categories": categories})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'post' : post})

def archives(request) :             #归档
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

def aboutme(request) :
    return render_to_response('aboutme.html')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(tag__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render_to_response('tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render_to_response('home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render_to_response(request, 'archives.html', {'post_list' : post_list,
                                                    'error' : False})
            else :
                return render_to_response(request, 'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.published_date

    def item_description(self, item):
        return item.text


def post_list_by_category(request, cg):
    """根据目录列表已发布文章"""
    posts = Article.objects.annotate(num_comment=Count('comment')).filter(
        published_date__isnull=False, category__name=cg).prefetch_related(
        'category').order_by('-published_date')
    # for p in posts:
    #     p.click = cache_manager.get_click(p)
    return render_to_response('home.html', {'posts': posts,"is_category": True,
                                'list_header': '\'{}\' 分类的存档'.format(cg)},
                              context_instance=RequestContext(request))


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "published_date"
    allow_future = True

    def viewdate(request):
        """根据目录列表已发布文章"""
        posts = Article.objects.annotate(num_comment=Count('comment')).filter(
            published_date__isnull=True).prefetch_related(
            'category').order_by('-published_date')
        # for p in posts:
        #     p.click = cache_manager.get_click(p)
        return render_to_response('date.html', {'posts': posts,"is_category": True},
                                  context_instance=RequestContext(request))
