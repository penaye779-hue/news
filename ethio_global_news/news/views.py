from django.shortcuts import render, get_object_or_404
from .models import Newsletter, Category
from django.shortcuts import render, get_object_or_404
from .models import Newsletter
from django.core.paginator import Paginator
from .models import News
from .forms import NewsForm
from django.shortcuts import render, redirect

# Home page: list of all news (latest first)
from django.shortcuts import render
from .models import News, Category

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

# News detail page
def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    categories = Category.objects.all()
    
    return render(request, 'news/news_detail.html', {
        'news_item': news_item,
        'categories': categories
    })
def news_list(request):
    all_news = News.objects.all().order_by('-created_at')  # adjust field name
    return render(request, 'news_list.html', {'all_news': all_news})
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_create.html', {'form': form})

# Category-specific news
def category_news(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news_list = category.news.all().order_by('-created_at')
    return render(request, 'news/home.html', {'news_list': news_list, 'category': category})

# Newsletter subscription
def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            Subscriber.objects.get_or_create(email=email)
    return redirect('home')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # You can save email to a model or a file here
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "Please enter a valid email.")
    return redirect('home')

# News CRUD operations
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})

def news_edit(request, id):
    news_item = get_object_or_404(News, pk=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news_item)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'news/news_form.html', {'form': form})

def news_delete(request, id):
    news_item = get_object_or_404(News, pk=id)
    news_item.delete()
    return redirect('home')
def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/news_create.html', {'form': form})