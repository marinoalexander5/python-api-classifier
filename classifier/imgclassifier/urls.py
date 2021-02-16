from django.urls import path
from .views import classifier_detail_view, classifier_list_view, classifier_create_view, classifier_update_view, classifier_delete_view

app_name = 'imgclassifier'
urlpatterns = [

    path('',classifier_list_view),
    path('classifier/<int:pk>/',classifier_detail_view),
    path('classifier/create/',classifier_create_view),
    path('classifier/<int:pk>/update/',classifier_update_view),
    path('classifier/<int:pk>/delete/',classifier_delete_view)
  
]