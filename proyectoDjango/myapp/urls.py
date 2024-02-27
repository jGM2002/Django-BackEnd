from django.urls import path
from . import views

urlpatterns = [
    path('api/ListAll_Customer', views.CustomerAllViewSet.as_view()),
    path('api/Create_Customer', views.CustomerCreate.as_view()),
    path('api/Delete_Customer/<customer_id>', views.CustomerDelete.as_view()),
    path('api/Update_Customer/<customer_id>', views.CustomerUpdate.as_view()),
]