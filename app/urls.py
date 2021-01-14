from django.urls import path
from .views import (index,
                    create_company,
                    update_company,
                    delete_company,
                    list_service_orders,
                    create_service_order,
                    create_service)

urlpatterns = [
    path('', index, name='index'),
    path('new/', create_company, name='create_company'),
    path('update/<int:id>', update_company, name='update_company'),
    path('delete/<int:id>', delete_company, name='delete_company'),
    path('so/<int:id>', list_service_orders, name='list_service_orders'),
    path('new_so/', create_service_order, name='create_service_order'),
    path('new_service/', create_service, name='create_service'),
]