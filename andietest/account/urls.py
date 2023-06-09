from django.urls import path

from . import views

urlpatterns = [
  path("create-account/", views.create_account, name="create_account"),
  path("delete-account/", views.delete_account, name="delete_account"),
  path("create-business/", views.create_business, name="create_business"),
  path("delete-business/", views.delete_business, name="delete_business"),
  path("create-item/", views.create_item, name="create_item"),
  path("delete-item/", views.delete_item, name="delete_item"),
  path("edit-item/", views.edit_item, name="edit_item"),
  path("login/", views.login, name="login"),
  path("update-activity/", views.update_activity, name="update_activity"),
  path("create-order/", views.create_order, name="create_order"),
  path("get-all-orders/", views.get_all_orders, name="get_all_orders"),
  path("get-orders-by-id/", views.get_orders_by_id, name="get_orders_by_id"),
]