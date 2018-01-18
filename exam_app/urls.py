from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from exam_app.views import ProductView, OrderView, UserView


router = DefaultRouter()
router.register(r'products', ProductView)
router.register(r'order', OrderView)
router.register(r'users', UserView)


urlpatterns = [
    # Auth:
    url(r'^auth/$', obtain_jwt_token),

    # Other endpoints:
    url(r'', include(router.urls))
]
