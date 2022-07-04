from django.db import router
from django.urls import  path
from appAPI.views import TodoViewSet, AgendamentoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'', TodoViewSet)
router.register(r'', AgendamentoViewSet)
urlpatterns = router.urls



