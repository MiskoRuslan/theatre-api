from django.urls import path, include
from rest_framework import routers

from theatre_service_app.views import GenreViewSet, ActorViewSet, TheatreHallViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", TheatreHallViewSet)
# router.register("movies", MovieViewSet)
# router.register("movie_sessions", MovieSessionViewSet)
# router.register("orders", OrderViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre_app"
