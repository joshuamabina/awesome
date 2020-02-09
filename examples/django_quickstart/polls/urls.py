from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # GET /polls
    path('', views.index, name='index'),

    # POST /polls/new
    path('new/', views.store, name='store'),

    # GET /polls/<question_id>/show
    path('<int:question_id>/show', views.show, name='show'),

    # PATCH /polls/<question_id>/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
]
