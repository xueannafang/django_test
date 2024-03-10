from django.urls import path

from . import views
#from current working directory import views.py

#create a url from the function index in views.py
app_name = "polls" #set the application namespace

#question_id can be replaced by primary key (pk)

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("specifics/<int:question_id>/", views.details, name="detail"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name = "vote"),
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("<int:pk>/", views.DetailView.as_view(), name = "detail"), 
    path("<int:pk>/results", views.ResultsView.as_view(), name = "results"),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
]
# the views also need to be amended