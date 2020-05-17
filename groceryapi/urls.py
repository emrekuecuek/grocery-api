from django.urls import path, include
from rest_framework import routers
from. import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'transactions', views.TransactionStoryViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls))
    # path("", views.index, name="index"),
    # path("products/<int:product_id>/", views.get_product_by_id, name="get_product_by_id"),
    # path("users/user_id/<int:user_id>/", views.get_user_by_id, name="get_user_by_id"),
    # path("users/customer_id/<int:customer_id>/", views.get_user_by_customer_id, name="get_user_by_customer_id"),
    # path("transactionstory/customer_id/<int:customer_id>/", views.get_transactions_story_by_customer_id, name="get_transactions_story_by_customer_id"),



    ]
