from django.urls import path

from .api_endpoints import FrontendTranslationAPIView, VersionHistoryAPIView

app_name = "common"

urlpatterns = [
    path("frontend-translations/", FrontendTranslationAPIView.as_view(), name="frontend-translations"),
    path("version-history/", VersionHistoryAPIView.as_view(), name="version-history"),
]
