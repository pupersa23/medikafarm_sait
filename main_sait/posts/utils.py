from django.core.paginator import Paginator


POST_LIMIT = 6


def paginator(request, posts):
    paginator = Paginator(posts, POST_LIMIT)
    page_number = request.GET.get('page')
    paje_obj = paginator.get_page(page_number)
    return paje_obj
