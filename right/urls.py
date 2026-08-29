from django.urls import path
from . import views

app_name = 'right'  # Important for namespacing in {% url %}

urlpatterns = [
    path('', views.rights, name='rights_list'),  # → rights.html
    path('<str:tn>/', views.article, name='rights_sections'),  # → section.html
    path('<str:tn>/section/<int:no>/', views.right_detail, name='right_detail'),  # → rightdetail.html
]
