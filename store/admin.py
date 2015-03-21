from django.contrib import admin
from django.db import models
from django import forms

from .models import Store, Locality, Brand_Chains, Financial_Chains, Payment_Types

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    # date_hierarchy = 'timestamp'  # updated
    fieldsets = (
        (None, {
            'fields': ('store_name', 'store_address', ('store_locality_city', 'store_pincode',),
                       ('store_status', 'store_type'), 'store_display_order',
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

    search_fields = ['store_name', 'store_locality_city']
    list_display = ['store_name', 'store_locality_city', 'store_type', 'store_address',
                    'store_status','store_display_order']
    list_editable = ['store_locality_city', 'store_type', 'store_address',
                     'store_status','store_display_order']
    list_filter = ['store_locality_city__city','store_locality_city__locality', 'store_status', 'store_type']
    readonly_fields = ['store_added_by','store_added_time','store_updated_by', 'store_updated_time']
    # prepopulated_fields = {'store_slug': ('store_name', 'store_locality_city',)}
    exclude = ['store_country']

    class Meta:
        model = Store



class LocalityAdmin(admin.ModelAdmin):

    search_fields = ['locality',]
    list_filter = ['city',]
    list_display = ['city','locality',]
    list_editable = ['locality',]

    class Meta:
        model = Locality

class BrandChainsAdmin(admin.ModelAdmin):

    search_fields = ['brand_name',]
    list_filter = ['brand_status',]
    list_display = ['brand_name', 'brand_status',]
    list_editable = ['brand_status',]
    readonly_fields = ['brand_added_by','brand_added_time','brand_updated_by', 'brand_updated_time']

    class Meta:
        model = Brand_Chains

class FinancialChainAdmin(admin.ModelAdmin):

    search_fields = ['financial_brand_name',]
    list_filter = ['financial_brand_status',]
    list_display = ['financial_brand_name', 'financial_brand_status',]
    list_editable = ['financial_brand_status',]
    readonly_fields = ['financial_brand_added_by','financial_brand_added_time',
                       'financial_brand_updated_by', 'financial_brand_updated_time']

    class Meta:
        model = Financial_Chains

class PaymentTypeAdmin(admin.ModelAdmin):

    search_fields = ['payment_type_name',]
    list_filter = ['payment_type_status',]
    list_display = ['payment_type_name', 'payment_type_status',]
    list_editable = [ 'payment_type_status',]
    readonly_fields = ['payment_type_added_by','payment_type_added_time',
                       'payment_type_updated_by', 'payment_type_updated_time']

    class Meta:
        model = Payment_Types


admin.site.register(Store, StoreAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Brand_Chains,BrandChainsAdmin)
admin.site.register(Financial_Chains,FinancialChainAdmin)
admin.site.register(Payment_Types,PaymentTypeAdmin)
