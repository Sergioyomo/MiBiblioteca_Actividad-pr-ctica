from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal' ),
    path('<int:pk>', views.detalle_libro, name='detalle_libro'),
]