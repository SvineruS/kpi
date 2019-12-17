from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_view, name="index"),

    # lab 1
    path('Home/Calc', views.calc_view, name="calc"),

    # lab 2
    path('Home/', views.get_all_contacts_view, name="get_all"),
    path('Home/Details/<id>/', views.get_contact_view, name="get"),

    # lab 3
    path('Home/Create', views.create_contact_view, name="create"),
    path('Home/Edit/<id>/', views.edit_contact_view, name="edit"),
    path('Home/Delete/<id>/', views.delete_contact_view, name="delete"),

    path('Home/Create/Approve/', views.create_contact_post, name="create_post"),
    path('Home/Edit/Approve/<id>/', views.edit_contact_post, name="edit_post"),
    path('Home/Delete/Approve/<id>/', views.delete_contact_post, name="delete_post"),

    # lab 4
    path('api/WApi/GetGroups', views.WApi_GetAll_view, name="wapi_get_all"),
    path('api/WApi/<id>', views.WApi_Get_view, name="wapi_get"),

    # lab 5
    path('api/WApi/CreateGroup/', views.WApi_Create_view, name="wapi_create"),
    path('api/WApi/UpdateGroup/', views.WApi_Update_view, name="wapi_update"),
    path('api/WApi/DeleteGroup/', views.WApi_Delete_view, name="wapi_delete"),

]
