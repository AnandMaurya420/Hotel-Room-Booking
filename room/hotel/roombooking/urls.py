from django.urls import path
from .views import hotel_register,show_hotels,hotel_update,hotel_delete, customer_register,customer_get, customer_update, customer_delete
from . import views

urlpatterns = [
    # ------------- hotel - url -------------- 

    path('hotelregister/',views.hotel_register),
    path('showhotel/<int:id>/',views.show_hotels),
    path('updatehotel/<int:id>/',views.hotel_update),
    path('deletehotel/<int:id>/',views.hotel_delete),

    # ------- customer url--------------
    path('customerregister/',views.customer_register),
    path('customerupdate/<int:id>/',views.customer_update),
    path('customerget/<int:id>/',views.customer_get),
    path('customerdelete/<int:id>/',views.customer_delete),

    # ------------ room --------------------------

    path('roomregister/',views.room_details),
    path('roomupdate/<int:id>/',views.room_update),
    path('roomget/<int:id>/',views.room_get),

    # -------- booking ---------------------------

    path('booking/',views.booking),

    # ----------- payment ------------------------
    path('payment/',views.payment),
]