from django.core.paginator import Paginator
from .models import Item
# contains all utility functions


def paginate_data(request, data):
    #  paginate through the given data
    page_number = request.GET.get('page')
    paginator = Paginator(data, 10)
    return paginator.get_page(page_number)


def get_searched_item(request, news, context):
    '''filter item by search 
    if found, returns the searched item
    else, returns the news object passed
    '''

    query = request.GET.get('search', None)
    if query:
        news = Item.objects.filter(title__icontains=query)
        if news:
            context['news'] = paginate_data(request, news)
            context['searched'] = True
            context['title'] = f"search - {query}"
    else:
        context['news'] = paginate_data(request, news)
    return context
