from django.urls import path, include
from rest_framework import routers

from theatre_service_app.views import GenreViewSet, ActorViewSet, TheatreHallViewSet, PlayViewSet, PerformanceViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_halls", TheatreHallViewSet)
router.register("plays", PlayViewSet)
router.register("performance", PerformanceViewSet)
# router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre_app"
