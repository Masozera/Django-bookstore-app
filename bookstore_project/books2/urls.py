from django.urls import path
from .views import BookListView,BookDetailView, SearchResultsListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    # path('<int:pk>', BookDetailView.as_view(), name='book_detail'), # new
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'), # new
    path('search/', SearchResultsListView.as_view(), name='search_results') # new implementint the search query

]
