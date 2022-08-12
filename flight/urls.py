from xml.etree.ElementInclude import include
from rest_framework import routers
from .views import FlightView

router = routers.DefaultRouter()
router.register('flights', FlightView)


urlpatterns = [
    # path('', include(router.urls))
]

urlpatterns += router.urls