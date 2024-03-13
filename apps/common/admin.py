from django.contrib import admin

from apps.common.models import FrontendTranslation, VersionHistory


@admin.register(VersionHistory)
class VersionHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "version", "required", "created_at", "updated_at")
    list_display_links = ("id", "version")
    list_filter = ("required",)
    search_fields = ("version",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(FrontendTranslation)
class FrontTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "text", "created_at", "updated_at")
    list_display_links = ("id", "key")
    search_fields = ("key", "text")
    readonly_fields = ("created_at", "updated_at")
