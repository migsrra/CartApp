from django.urls import path

from . import views

#Note: As stated in some views.py functions, the url paths that contain /<int:...>/
#are used to retrieve function parameters. If you would like to use the Postman query parameters instead,
#remove the /<int:...>/ from these urlpaths, and remove the respective parameters from their function headers.
#Both ways work the same way.

urlpatterns = [
    path("",views.index,name="index"),
    path("create-account/",views.createAccount,name="create-account"),
    path("delete-account/<int:accountID>/",views.deleteAccount,name="delete-account"),
    path("login/",views.login,name="login"),
    path("edit-activity/<int:accountID>/",views.editActivity,name="edit-activity"),
    path("create-business/",views.createBusiness,name="create-business"),
    path("delete-business/<int:businessID>/",views.deleteBusiness,name="delete-business"),
    path("create-item/<int:businessID>/",views.createInventoryItem,name="create-item"),
    path("delete-item/<int:inventoryID>/",views.deleteInventoryItem,name="delete-item"),
    path("edit-item/<int:inventoryID>/",views.editInventoryItem,name="edit=item"),
    path("create-order/<int:businessID>/<int:accountID>/",views.createOrder,name="create-order"),
    path("get-orders/",views.getAllOrders,name="get-orders"),
    path("get-account-orders/<int:accountID>/",views.getAccountOrders,name="get-account-orders"),
    path("get-order-total/<int:orderID>/",views.getOrderTotal,name="get-order-total"),
]