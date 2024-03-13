from django.urls import path

from .api_endpoints import FrontendTranslationAPIView, VersionHistoryAPIView

app_name = "common"

urlpatterns = [
    path("FrontendTranslations/", FrontendTranslationAPIView.as_view(), name="frontend-translations"),
    path("VersionHistory/", VersionHistoryAPIView.as_view(), name="version-history"),
]
