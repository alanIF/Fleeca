from django.urls import path,re_path

from finance import views
urlpatterns = [
    re_path("^$", views.index, name="index"),
    path("wallet/add", views.add_wallet, name="add_wallet"),
    path("wallet/edit/<int:wallet_id>", views.edit_wallet, name="edit_wallet"),
    path("wallet/delete/<int:wallet_id>", views.delete_wallet, name="delete_wallet"),

    path("type/", views.index_type, name="index_type"),
    path("type/add", views.add_type, name="add_type"),
    path("type/edit/<int:type_id>/", views.edit_type, name="edit_type"),
    path("type/delete/<int:type_id>/", views.delete_type, name="delete_type"),

    path("wallet/<int:wallet_id>", views.view_wallet, name="view_wallet"),
    path("wallet/<int:wallet_id>/add", views.add_moviment_walet, name="add_moviment_wallet"),
    path("wallet/<int:wallet_id>/delete/<int:moviment_id>", views.delete_moviment_walet, name="delete_moviment_wallet"),
    path("wallet/<int:wallet_id>/edit/<int:moviment_id>", views.edit_moviment_walet, name="edit_moviment_wallet"),


]
