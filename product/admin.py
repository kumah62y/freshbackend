from django.contrib import admin

from .models import Product,Brand,Category,SubCategory,SubCategory_Attached,Product_Unit


class CategoryAttachedInline(admin.TabularInline):

    model = SubCategory_Attached
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    # date_hierarchy = 'timestamp'  # updated
    fieldsets = (
        (None, {
            'fields': (('product_name', 'product_brand',), ('product_featured', 'product_status',),
                       ('product_SKU', 'product_MRP',), ('product_slug', 'product_meta',),
                       ('product_primary_unit', 'product_secondary_unit',), ('product_tax_code',),
                       ('product_short_description',),
            )
        }),

        ('Other Details', {
            'classes': ('collapse',),
            'fields': (('product_added_by','product_added_time'),
                       ('product_updated_by','product_updated_time'),
                      )
        }),
    )

    search_fields = ['product_name', 'product_brand','product_meta','product_short_description']
    list_display = ['product_name', 'product_brand', 'product_SKU', 'product_status',
                    'product_primary_unit',]
    list_editable = ['product_brand', 'product_SKU', 'product_status',
                    'product_primary_unit',]
    list_filter = ['product_brand__brand_name','product_category__category_name',]
    readonly_fields = ['product_added_by','product_added_time','product_updated_by', 'product_updated_time']
    inlines = (CategoryAttachedInline,)

    save_as = True
    # prepopulated_fields = {'store_slug': ('store_name', 'store_locality_city',)}
    # exclude = ['store_country']

    class Meta:
        model = Product


class BrandAdmin(admin.ModelAdmin):

    search_fields = ['brand_name',]
    list_filter = ['brand_status',]
    list_display = ['brand_name','brand_status',]
    list_editable = ['brand_name',]
    readonly_fields = ['brand_added_by','brand_added_time','brand_updated_by', 'brand_updated_time']

    class Meta:
        model = Brand

class CategoryAdmin(admin.ModelAdmin):

    search_fields = ['category_name','category_description']
    list_filter = ['category_status','category_featured']
    list_display = ['category_name','category_status','category_featured']
    list_editable = ['category_status','category_featured',]
    readonly_fields = ['category_added_by','category_added_time','category_updated_by', 'category_updated_time']
    inlines = (CategoryAttachedInline,)


    class Meta:
        model = Category


class SubCategoryAdmin(admin.ModelAdmin):

    search_fields = ['subcategory_name','subcategory_description']
    list_filter = ['category__category_name','subcategory_status','subcategory_featured']
    list_display = ['subcategory_name','category','subcategory_status','subcategory_featured']
    list_editable = ['category','subcategory_status','subcategory_featured',]
    readonly_fields = ['subcategory_added_by','subcategory_added_time','subcategory_updated_by',
                       'subcategory_updated_time']

    class Meta:
        model = SubCategory


class Product_UnitAdmin(admin.ModelAdmin):

    search_fields = ['product_unit_name',]
    list_filter = ['product_unit_status',]
    list_display = ['product_unit_name','product_unit_status',]
    list_editable = ['product_unit_name',]
    readonly_fields = ['product_unit_added_by','product_unit_added_time','product_unit_updated_by',
                       'product_unit_updated_time']

    class Meta:
        model = Product_Unit



admin.register(Product,ProductAdmin)
admin.register(Brand,BrandAdmin)
admin.register(Category,CategoryAdmin)
admin.register(SubCategory,SubCategoryAdmin)
admin.register(Product_Unit,Product_UnitAdmin)