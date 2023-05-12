from django.urls import path

from . import views

urlpatterns = [
  path("create-account/", views.create_account, name="create_account"),
  path("delete-account/", views.delete_account, name="delete_account"),
  path("create-business/", views.create_business, name="create_business"),
  path("delete-business/", views.delete_business, name="delete_business"),
  path("create-item/", views.create_item, name="create_item"),
  path("delete-item/", views.delete_item, name="delete_item"),
]