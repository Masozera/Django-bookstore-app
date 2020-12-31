from django.db import models
import uuid # new
from django.urls import reverse
from django.contrib.auth import get_user_model # new

class Book(models.Model):
    # id = models.UUIDField( primary_key=True default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='pics/', blank=True) # new

    class Meta: # new
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        #return reverse('book_detail', args=[str(self.id)])
        return reverse('book_detail', kwargs={'pk': str(self.pk)})

class Review(models.Model): # new
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews',) # The book field is the one-tomany foreign key that links Book to Review and we’re following the standard practice of naming it the same as the linked model.
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,) # And then we’ll also link to the author field to auto-populate the current user with the review.

    def __str__(self):
        return self.review