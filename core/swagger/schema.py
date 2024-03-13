from django.urls import re_path

from core.swagger.utils import main_schema_view

swagger_urlpatterns = [
    re_path("swagger-without-ui/", main_schema_view.without_ui(cache_timeout=0), name="schema-json"),  # noqa
    re_path(
        r"^swagger/$",
        main_schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path("redoc/", main_schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),  # noqa
]
