from django.contrib import admin
from django.db import models
from django import forms

from store.models import Store, Locality, Brand_Chains, Financial_Chains, Payment_Types

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    # date_hierarchy = 'timestamp'  # updated
    fieldsets = (
        (None, {
            'fields': ('store_name', 'store_address', ('store_locality', 'store_city', 'store_pincode',),
                       ('store_status', 'store_type'), 'store_slug','store_display_order',
            )
        }),
        ('Contact Information', {
            'classes': ('collapse'),
            'fields': (('store_phone_number', 'store_order_number',), ('store_manager_number', 'store_owner_number',
                                                                       'store_owner_email',),
            )
        }),
        ('Geo Co-ordinates', {
            'classes': ('collapse',),
            'fields': (('store_latitude', 'store_longitude',),)
        }),
        ('Store Opening Timing', {
            'classes': ('collapse',),
            'fields': (('store_open_monday', 'store_open_tuesday', 'store_open_wednesday', 'store_open_thursday',),
                       ('store_open_friday', 'store_open_saturday', 'store_open_sunday',),)
        }),

        ('Store Closing Timing', {
            'classes': ('collapse',),
            'fields': (('store_close_monday', 'store_close_tuesday', 'store_close_wednesday', 'store_close_thursday',),
                       ('store_close_friday', 'store_close_saturday', 'store_close_sunday',),)
        }),

        ('Store Delivery Start', {
            'classes': ('collapse',),
            'fields': (('store_delivery_start_monday', 'store_delivery_start_tuesday', 'store_delivery_start_wednesday',
                        'store_delivery_start_thursday',),('store_delivery_start_friday',
                        'store_delivery_start_saturday', 'store_delivery_start_sunday',),)
        }),

        ('Store Delivery Close', {
            'classes': ('collapse',),
            'fields': (('store_delivery_close_monday', 'store_delivery_close_tuesday',
                        'store_delivery_close_wednesday', 'store_delivery_close_thursday',),
                       ('store_delivery_close_friday', 'store_delivery_close_saturday',
                        'store_delivery_close_sunday',),)
        }),

        ('Other Details', {
            'classes': ('collapse',),
            'fields': (('store_sales_rep', 'store_account_manager',),
                       ('store_delivery_area_primary', 'store_min_order_primary',),
                       ('store_delivery_area_secondary', 'store_min_order_secondary',),
                       ('store_payment_cycle','store_bank_account',),
                       ('store_associated_brand_chain','store_associated_financial_chain',),
                       ('store_payment_methods',),
                       ('store_added_by','store_added_time'),
                       ('store_updated_by','store_updated_time'),
                        )
        }),
    )

    search_fields = ['store_name', 'store_locality']
    list_display = ['store_name', 'store_locality', 'store_type', 'store_address', 'store_status','store_display_order']
    list_editable = ['store_name', 'store_locality', 'store_type', 'store_address', 'store_status','store_display_order']
    list_filter = ['store_locality', 'store_status', 'store_type']
    readonly_fields = ['store_added_by','store_added_time','store_updated_by', 'store_updated_time']
    prepopulated_fields = {'store_slug': ('store_name', 'store_locality',)}
    exclude = ['store_country']

    class Meta:
        model = Store


admin.site.register(Store, StoreAdmin)
admin.site.register(Locality)
admin.site.register(Brand_Chains)
admin.site.register(Financial_Chains)
admin.site.register(Payment_Types)
