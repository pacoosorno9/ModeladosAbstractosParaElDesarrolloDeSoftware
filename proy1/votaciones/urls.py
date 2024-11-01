from django.urls import path 
from  . import views

app_name = "votaciones"

urlpatterns = [
    #/votaciones/
    path("", views.IndexViews.as_view(), name = "Index"),
    #/votaciones/10/
    path("<int:pregunta_id>/", views.DetailView.as_view(), name="detail"),
    #/votacioenes/10/results
    path("<int:pregunta_id>/results/", views.ResultsView.as_view(), name="results"),
    #/votaciones/10/vote/
    path("<int:pregunta_id>/vote/", views.vote, name="vote")
]