from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from . import views

router = DefaultRouter()
router.trailing_slash = '/?'
router.register(r'transaction', views.TransactionViewSet, basename='transaction')
app_name = 'transaction'

urlpatterns = [
    url('', include(router.urls))
]
