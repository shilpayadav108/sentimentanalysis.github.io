from django.contrib import admin

# Register your models here.
from .models import IndexView,FeedbackCreateView, ReviewsListView,ReviewDetailsView
admin.site.register(IndexView)
admin.site.register(FeedbackCreateView)
admin.site.register(ReviewsListView)
admin.site.register(ReviewDetailsView)
