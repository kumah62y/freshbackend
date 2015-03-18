from django.db import models

# Create your models here.



class Store(models.Model):
    CITY_CHOICES = (
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Gurgaon', 'Gurgaon'),
        ('Noida', 'Noida'),
    )

    COUNTRY_CHOICES = (
        ('India', 'India'),
    )

    STORE_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )

    STORE_TYPE = (
        ('Fruits & Vegetables', 'Fruits & Vegetables'),
        ('Grocery', 'Grocery'),
        ('Bakery', 'Bakery'),
        ('Meat', 'Meat'),
        ('Flowers', 'Flowers')
    )

    store_name = models.CharField(max_length=100, help_text='Enter Store Name', verbose_name='Store Name')
    store_address = models.CharField(max_length=200, verbose_name='Store Address')
    store_locality = models.ForeignKey('Locality', verbose_name='Store Locality')
    store_city = models.CharField(max_length=100, choices=CITY_CHOICES, default='Mumbai', verbose_name='Store City')
    store_country = models.CharField(max_length=100, default='India', choices=COUNTRY_CHOICES,
                                     verbose_name='Store Country')
    store_pincode = models.CharField(max_length=10, default=201301, verbose_name='Store PINCODE')
    store_status = models.CharField(max_length=100, default='Active', verbose_name='Status',choices=STORE_STATUS_CHOICES)

    store_type = models.CharField(max_length=50, choices=STORE_TYPE, default='Grocery', verbose_name='Store Type')

    store_slug = models.SlugField(unique=True, verbose_name='Store Slug')

    store_phone_number = models.CharField(max_length=20,blank=True, verbose_name='Store Phone Number')
    store_order_number = models.CharField(max_length=20,blank=True, verbose_name='Store Order Number')
    store_manager_number = models.CharField(max_length=20,blank=True, verbose_name='Store Manager Number ')
    store_owner_number = models.CharField(max_length=20,blank=True, verbose_name='Store Owner Number')
    store_owner_email = models.EmailField(null=True,verbose_name='Store Owner Email')

    store_latitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True,
                                         verbose_name='Store Latitude')
    store_longitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True,
                                          verbose_name='Store Longitude')


    # Store opening timings

    store_open_monday = models.TimeField(verbose_name='Store Open Time Monday',default='09:30')
    store_close_monday = models.TimeField(verbose_name='Store Close Time Monday',default='21:30')

    store_open_tuesday = models.TimeField(verbose_name='Store Open Time Tuesday',default='09:30')
    store_close_tuesday = models.TimeField(verbose_name='Store Close Time Tuesday',default='21:30')

    store_open_wednesday = models.TimeField(verbose_name='Store Open Time Wednesday',default='09:30')
    store_close_wednesday = models.TimeField(verbose_name='Store Close Time Wednesday',default='21:30')

    store_open_thursday = models.TimeField(verbose_name='Store Open Time Thursday',default='09:30')
    store_close_thursday = models.TimeField(verbose_name='Store Close Time Thursday',default='21:30')

    store_open_friday = models.TimeField(verbose_name='Store Open Time Friday',default='09:30')
    store_close_friday = models.TimeField(verbose_name='Store Close Time Friday',default='21:30')

    store_open_saturday = models.TimeField(verbose_name='Store Open Time Saturday',default='09:30')
    store_close_saturday = models.TimeField(verbose_name='Store Close Time Saturday',default='21:30')

    store_open_sunday = models.TimeField(verbose_name='Store Open Time Sunday',default='09:30')
    store_close_sunday = models.TimeField(verbose_name='Store Close Time Sunday',default='21:30')

    # Store delivery timings

    store_delivery_start_monday = models.TimeField(verbose_name='Store Delivery Start Time Monday',default='09:30')
    store_delivery_close_monday = models.TimeField(verbose_name='Store Delivery Close Time Monday',default='21:30')

    store_delivery_start_tuesday = models.TimeField(verbose_name='Store Delivery Start Time Tuesday',default='09:30')
    store_delivery_close_tuesday = models.TimeField(verbose_name='Store Delivery Close Time Tuesday',default='21:30')

    store_delivery_start_wednesday = models.TimeField(verbose_name='Store Delivery Start Time Wednesday',default='09:30')
    store_delivery_close_wednesday = models.TimeField(verbose_name='Store Delivery Close Time Wednesday',default='21:30')

    store_delivery_start_thursday = models.TimeField(verbose_name='Store Delivery Start Time Thursday',default='09:30')
    store_delivery_close_thursday = models.TimeField(verbose_name='Store Delivery Close Time Thursday',default='21:30')

    store_delivery_start_friday = models.TimeField(verbose_name='Store Delivery Start Time Friday',default='09:30')
    store_delivery_close_friday = models.TimeField(verbose_name='Store Delivery Close Time Friday',default='21:30')

    store_delivery_start_saturday = models.TimeField(verbose_name='Store Delivery Start Time Saturday',default='09:30')
    store_delivery_close_saturday = models.TimeField(verbose_name='Store Delivery Close Time Saturday',default='21:30')

    store_delivery_start_sunday = models.TimeField(verbose_name='Store Delivery Start Time Sunday',default='09:30')
    store_delivery_close_sunday = models.TimeField(verbose_name='Store Delivery Close Time Sunday',default='21:30')

    store_sales_rep = models.CharField(max_length=100,blank=True, verbose_name='Sales Representative')
    store_account_manager = models.CharField(max_length=100,blank=True, verbose_name='Account Manager')

    store_delivery_area_primary = models.PositiveSmallIntegerField(verbose_name='Primary Delivery Radius KM:',default=2)
    store_min_order_primary = models.PositiveSmallIntegerField(verbose_name='Minimum Order Primary Radius',default=200)

    store_delivery_area_secondary = models.PositiveSmallIntegerField(verbose_name='Secondary Delivery Radius',default=5)
    store_min_order_secondary = models.PositiveSmallIntegerField(verbose_name='Minimum Order Secondary Radius',
                                                                 default=500)

    store_payment_cycle = models.PositiveSmallIntegerField(verbose_name='Payment Cycle', null=True, blank=True)
    store_bank_account = models.CharField(max_length=100, verbose_name='Bank Account', blank=True)

    store_associated_brand_chain = models.ForeignKey('Brand_Chains', null=True, blank=True,
                                                     verbose_name='Associated Brand')
    store_associated_financial_chain = models.ForeignKey('Financial_Chains', null=True, blank=True,
                                                         verbose_name='Associated Brand')

    store_payment_methods = models.ManyToManyField('Payment_Types', verbose_name='Payment Types', null=True)

    store_display_order = models.SmallIntegerField(verbose_name='Display Order',
                                                   help_text='Please give a order number. Stores displayed as per this sorting ')

    store_added_by = models.CharField(verbose_name='Store Added By', blank=True, default='Admin', max_length=100)
    store_added_time = models.DateTimeField(verbose_name='Store Added Time', auto_now_add=True,blank=True,null=True)

    store_updated_by = models.CharField(verbose_name='Store Updated By', blank=True, default='Admin', max_length=100)
    store_updated_time = models.DateTimeField(verbose_name='Store Update Time', auto_now=True,blank=True,null=True)

    def __str__(self):
        return '%s - %s' % (self.store_name, self.store_locality)


    class Meta:
        ordering = ['store_locality']
        unique_together = ('store_name', 'store_locality', 'store_city',)
        index_together = [
            ['store_locality', 'store_city'],
        ]
        verbose_name = "Store"
        verbose_name_plural = "Stores"


class Locality(models.Model):
    city = models.CharField(max_length=100, choices=Store.CITY_CHOICES)
    locality = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s' % (self.city, self.locality)

    class Meta:
        ordering = ['city','locality']
        verbose_name = "Locality"
        verbose_name_plural = "Localities"

class Brand_Chains(models.Model):

    BRAND_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )


    brand_name = models.CharField(max_length=100, verbose_name='Brand Name')
    brand_status = models.CharField(max_length=100,choices=BRAND_STATUS_CHOICES, verbose_name='Status')

    brand_added_by = models.CharField(verbose_name='Brand Added By', blank=True, default='Admin', max_length=100)
    brand_added_time = models.DateTimeField(verbose_name='Brand Added Time', auto_now_add=True)

    brand_updated_by = models.CharField(verbose_name='Store Updated By', blank=True, default='Admin', max_length=100)
    brand_updated_time = models.DateTimeField(verbose_name='Store Update Time', auto_now=True)

    def __str__(self):
        return '%s' % (self.brand_name,)

    class Meta:
        ordering = ['brand_name']
        verbose_name = "Store Brand"
        verbose_name_plural = "Store Brands"

class Financial_Chains(models.Model):

    FINANCIAL_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )

    financial_brand_name = models.CharField(max_length=100, verbose_name='Financial Brand Name')
    financial_brand_status = models.CharField(max_length=100,choices=FINANCIAL_STATUS_CHOICES, verbose_name='Status')

    financial_brand_added_by = models.CharField(verbose_name='Financial Brand Added By', blank=True, default='Admin', max_length=100)
    financial_brand_added_time = models.DateTimeField(verbose_name='Financial Brand Added Time', auto_now_add=True)

    financial_brand_updated_by = models.CharField(verbose_name='Financial Store Updated By', blank=True, default='Admin', max_length=100)
    financial_brand_updated_time = models.DateTimeField(verbose_name='Financial Store Update Time', auto_now=True)

    def __str__(self):
        return '%s' % (self.financial_brand_name,)

    class Meta:
        ordering = ['financial_brand_name']
        verbose_name = 'Store Financial Brand'
        verbose_name_plural = 'Store Financial Brands'

class Payment_Types(models.Model):

    PAYMENT_TYPES_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )


    payment_type_name = models.CharField(max_length=100, verbose_name='Payment Type')
    payment_type_status = models.CharField(max_length=100,choices=PAYMENT_TYPES_STATUS_CHOICES, verbose_name='Status')

    payment_type_added_by = models.CharField(verbose_name='Payment Type Added By', blank=True, default='Admin', max_length=100)
    payment_type_added_time = models.DateTimeField(verbose_name='Payment Type Added Time', auto_now_add=True)

    payment_type_updated_by = models.CharField(verbose_name='Payment Type Updated By', blank=True, default='Admin', max_length=100)
    payment_type_updated_time = models.DateTimeField(verbose_name='Payment Type Update Time', auto_now=True)

    def __str__(self):
        return '%s' % (self.payment_type_name,)

    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'