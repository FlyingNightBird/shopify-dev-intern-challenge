"""tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from iteminfo.views import ItemList, ItemDetail, ItemCreate, ItemUpdate, ItemDelete, WarehouseList, WarehouseCreate, \
    WarehouseDetail, WarehouseUpdate, WarehouseDelete, AssignmentList, AssignmentDetail, AssignmentCreate, \
    AssignmentUpdate, AssignmentDelete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',
         RedirectView.as_view(
             pattern_name='iteminfo_item_list_urlpattern',
             permanent=False
         )),

    path('item/',
         ItemList.as_view(),
         name='iteminfo_item_list_urlpattern'),

    path('item/<int:pk>/',
         ItemDetail.as_view(),
         name='iteminfo_item_detailed_urlpattern'),

    path('item/create/',
         ItemCreate.as_view(),
         name='iteminfo_item_create_urlpattern'),

    path('item/<int:pk>/update/',
         ItemUpdate.as_view(),
         name='iteminfo_item_update_urlpattern'),

    path('item/<int:pk>/delete/',
         ItemDelete.as_view(),
         name='iteminfo_item_delete_urlpattern'),

    path('warehouse/',
         WarehouseList.as_view(),
         name='iteminfo_warehouse_list_urlpattern'),

    path('warehouse/<int:pk>/',
         WarehouseDetail.as_view(),
         name='iteminfo_warehouse_detailed_urlpattern'),

    path('warehouse/create/',
         WarehouseCreate.as_view(),
         name='iteminfo_warehouse_create_urlpattern'),

    path('warehouse/<int:pk>/update/',
         WarehouseUpdate.as_view(),
         name='iteminfo_warehouse_update_urlpattern'),

    path('warehouse/<int:pk>/delete/',
         WarehouseDelete.as_view(),
         name='iteminfo_warehouse_delete_urlpattern'),

    path('assignment/',
         AssignmentList.as_view(),
         name='iteminfo_assignment_list_urlpattern'),

    path('assignment/<int:pk>/',
         AssignmentDetail.as_view(),
         name='iteminfo_assignment_detailed_urlpattern'),

    path('assignment/create/',
         AssignmentCreate.as_view(),
         name='iteminfo_assignment_create_urlpattern'),

    path('assignment/<int:pk>/update/',
         AssignmentUpdate.as_view(),
         name='iteminfo_assignment_update_urlpattern'),

    path('assignment/<int:pk>/delete/',
         AssignmentDelete.as_view(),
         name='iteminfo_assignment_delete_urlpattern'),

]


