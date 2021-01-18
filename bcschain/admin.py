from django.contrib import admin
from .models import Block


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    fields = ['height', 'hash', 'timestamp', 'address', 'transactions']
