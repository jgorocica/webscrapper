from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from scrapy.crawler import CrawlerRunner
from .scraper import Scraper
from .models import Category, Links
from crochet import setup
from django.contrib.auth.decorators import login_required

setup()

# Create your views here.
@login_required
def load_links(request):
    if request.method == "GET":
        data = Category.objects.filter(user = request.user)
        paginator = Paginator(data, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "home.html", {"data": page_obj})
    else:
        return HttpResponse(status=405)

def show_links(request, category_id):
    if request.method == "GET":
        data = Links.objects.filter(category_id = category_id)
        return render(request, "links.html", {"data": data})
    else:
        return HttpResponse(status=405)

def scrap_link(request):
    """
        Add feature for scrap based on the link given
    """

    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    process = CrawlerRunner(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })
    process.crawl(Scraper, url=[data["url"]], user_id=request.user.id)
    # process.start(stop_after_crawl=True, install_signal_handlers=False)
    with open("items.json", "r") as f:
        data = f.read()

    return JsonResponse(data, safe=False)