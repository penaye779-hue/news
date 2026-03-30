from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from .models import News, Category, Subscriber
from .forms import NewsForm


# =========================
# HOME
# =========================
def home(request, category_id=None):
    latest_news = News.objects.all().order_by('-created_at')

    if category_id:
        latest_news = latest_news.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'news/home.html', {
        'latest_news': latest_news,
        'categories': categories,
        'selected_category_id': category_id
    })


# =========================
# NEWS DETAIL
# =========================
def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    categories = Category.objects.all()

    return render(request, 'news/news_detail.html', {
        'news_item': news_item,
        'categories': categories
    })


# =========================
# NEWS LIST
# =========================
def news_list(request):
    all_news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'all_news': all_news})


# =========================
# CREATE NEWS
# =========================
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()

    return render(request, 'news/news_create.html', {'form': form})


# =========================
# EDIT NEWS
# =========================
def news_edit(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
        return render(request, 'news/news_edit.html', {'form': form, 'news': news})

    form = NewsForm(instance=news)
    return render(request, 'news/news_edit.html', {'form': form, 'news': news})


# =========================
# DELETE NEWS
# =========================
def news_delete(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    news_item.delete()
    return redirect('home')


# =========================
# CATEGORY FILTER
# =========================
def category_news(request, category_id):
    latest_news = News.objects.filter(category_id=category_id).order_by('-created_at')
    categories = Category.objects.all()

    return render(request, 'news/home.html', {
        'latest_news': latest_news,
        'categories': categories,
        'selected_category_id': int(category_id),
    })


# =========================
# SUBSCRIBE
# =========================
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            Subscriber.objects.get_or_create(email=email)
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "Please enter a valid email.")

    return redirect('home')