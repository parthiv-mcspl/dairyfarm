from django.urls import path
from . import views

urlpatterns = [
    path('', views.combined_view, name='combined_view'),  # URL for the combined view
    path('book/', views.book_view, name='book'),  # URL: /book/
    path('reviews/', views.review_page, name='review_page'),
    path('contact/',views.for_contact, name='for_contact'),
]
