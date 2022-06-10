from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlowersView.as_view(), name='home'),
    path("filter/", views.FilterFlowersView.as_view(), name='filter'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('search/', views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.FlowersDetailView.as_view(), name='flowers_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]