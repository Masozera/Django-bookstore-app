from django.views.generic import ListView,DetailView
from .models import Book
# from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin # new
)

from django.db.models import Q # new


class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list' #  This subsittes object_list and make it user friendly
    template_name = 'books2/book_list.html'
    login_url = 'account_login' # new is setting a login_url for the user to be redirected to This is the URL name for log in which, since we’re using django-allauth is account_login

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): # new
    model = Book
    context_object_name = 'book' # new
    template_name = 'books2/book_detail.html'
    login_url = 'account_login' # new
    permission_required = 'books.special_status' # new This is for permissions specified in the model

class SearchResultsListView(ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books2/search_results.html'
    # queryset = Book.objects.filter(title__icontains='professionals') # new this queryset is default on the model.

    def get_queryset(self): # new
       # step is to take the user’s search
       # query, represented by q in the URL, and pass it in to the actual search filters.
       #query = self.request.GET.get('q')
        return Book.objects.filter(
            # Q(title__icontains='beginners') | Q(title__icontains='api')
                Q(title__icontains=query) | Q(author__icontains=query)

        )


#         What changed? We added a query variable that takes the value of q from the form
# submission. Then updated our filter to use query on either a title or an author field.



