from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'email', 'phone', 'created_at')
    list_filter = ('source', 'created_at')
    search_fields = ('email', 'phone', 'source')
    readonly_fields = ('source', 'payload', 'email', 'phone', 'created_at')
    date_hierarchy = 'created_at'
