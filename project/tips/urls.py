from rest_framework.routers import DefaultRouter
from tips import views
from django.urls import path,include
from django.conf.urls import url

app_name = "tips"
router = DefaultRouter()
#router.register(r'over', views.OverViewset, basename='over')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


from rest_framework.routers import DefaultRouter
from tips import views

router.register(r'over', views.OverViewset, basename='over')

urlpatterns = router.urls
