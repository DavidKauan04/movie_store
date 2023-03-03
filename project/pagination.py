from rest_framework.pagination import PageNumberPagination

class SourcePageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 50
    page_size_query_param = 'all'