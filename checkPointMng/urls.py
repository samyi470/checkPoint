from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # las
    path('las', views.las, name='las'),

    # lax
    path('lax', views.lax, name='lax'),

    # phx
    path('phx', views.phx, name='phx'),

    # data preparation
    path('datapreparation', views.datapreparation, name='datapreparation'),

    # passenger forecasting
    path('passengerforecasting', views.passengerforecasting, name='passengerforecasting'),
]

