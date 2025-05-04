from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.addbooks),
    path('bookdetails', views.bookdetails),
    # path('search', views.searchresult),
    # path('add/', views.add),
    # path('edit/<int:book_id>', views.edit),
    # path('delete/<int:book_id>', views.delete),
]