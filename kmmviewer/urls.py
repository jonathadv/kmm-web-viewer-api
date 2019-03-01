from django.urls import include, path
from rest_framework import routers
from kmm.views import TransactionsViewSet, SplitsViewSet, PayeeViewSet, AccountViewSet

router = routers.DefaultRouter()
router.register(r"transactions", TransactionsViewSet)
router.register(r"splits", SplitsViewSet)
router.register(r"payees", PayeeViewSet)
router.register(r"accounts", AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
