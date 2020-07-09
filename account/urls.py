from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from . import views

router = DefaultRouter()
router.trailing_slash = '/?'
router.register(r'account', views.AccountViewSet, basename='account')
app_name = 'account'

urlpatterns = [
    url('', include(router.urls))
]
