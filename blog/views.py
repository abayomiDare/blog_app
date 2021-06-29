from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import EmailPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def article_list(request):
    object_list =  Article.objects.filter(status='published')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:

        articles = paginator.page(1)
    except EmptyPage:

        articles = paginator.page(paginator.num_pages)
    context = {'page': page, 'articles': articles}
    return render(request, 'blog/article_list.html', context)


def article_detail(request, year, month, day, slug):
    article = get_object_or_404(Article, publish__year=year, publish__month=month,
                                publish__day=day, slug=slug, status='published')
    context = {'article': article}
    return render(request, 'blog/article_detail.html', context)




def article_share(request, post_id):
    
    articles = get_object_or_404(Article, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
            articles.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
            f"{articles.title}"
            message = f"Read {articles.title} at {post_url}\n\n" \
            f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'abayomi5991@gmail.com',
            [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {'articles': articles,'form': form,'sent': sent}
    return render(request, 'blog/share.html', context)
