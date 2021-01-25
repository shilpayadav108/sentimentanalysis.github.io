from django.urls import path
from . import Review
from .models import Review
from . import views
from .forms import ReviewForm


urlpatterns = [
   path('', views.IndexView, name='index'),
   path('review_sent/', views.FeedbackCreateView, name='review_sent'),
   path('reviews/', views.ReviewsListView, name='reviews'),
   path('reviews/<int:pk>/', views.ReviewDetailsView, name='review_details'),
]