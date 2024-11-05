from django.urls import include, path
from rest_framework.routers import DefaultRouter

from paper_graph.views import PaperViewSet

router = DefaultRouter()
router.register(r"papers", PaperViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
