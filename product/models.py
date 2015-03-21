from django.db import models




class Product(models.Model):

    PRODUCT_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )

    product_name = models.CharField(max_length=100,verbose_name='Product Name',)
    product_brand = models.ForeignKey('Brand',verbose_name='Product Brand',blank=True,null=True)
    product_featured = models.BooleanField(verbose_name='Featured Product',default=False,)
    product_status = models.CharField(verbose_name='Product Status',choices=PRODUCT_STATUS_CHOICES,default='Active')
    product_SKU = models.CharField(verbose_name='Product SKU',blank=True,unique=True,max_length=200)
    product_MRP = models.DecimalField(verbose_name='Product MRP', blank=True, null= True, decimal_places=2, max_digits=6)
    product_slug = models.SlugField(verbose_name='Product Slug', blank=True)
    product_meta = models.CharField(verbose_name='Product Meta', blank=True, max_length=300)
    product_primary_unit = models.ForeignKey('Product_Unit',blank=True, verbose_name='Product Main Unit')
    product_secondary_unit = models.ForeignKey('Product_Unit',blank=True, verbose_name='Product Secondary Unit')
    product_tax_code = models.CharField(verbose_name='Tax Code', blank=True, max_length=200)
    product_category = models.ManyToManyField('Category',verbose_name='Category', through='SubCategory_Attached')
    product_short_description = models.TextField(verbose_name='Description')

    product_added_by = models.CharField(verbose_name='Product Added By', blank=True, default='Admin', max_length=100)
    product_added_time = models.DateTimeField(verbose_name='Product Added Time', auto_now_add=True,blank=True,null=True)

    product_updated_by = models.CharField(verbose_name='Product Updated By', blank=True, default='Admin', max_length=100)
    product_updated_time = models.DateTimeField(verbose_name='Product Update Time', auto_now=True,blank=True,null=True)


    def __str__(self):
        return '%s - %s' % (self.product_name, self.product_brand)

    class Meta:
        # ordering = ['store_locality_city__city','store_locality_city__locality']
        # unique_together = ('store_name', 'store_locality_city',)
        # index_together = [
        #     ['store_locality', 'store_city'],
        # ]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Product_Unit(models.Model):

    PRODUCT_UNIT_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )


    product_unit_name = models.CharField(max_length=100, verbose_name='product_unit Name', unique=True)
    product_unit_status = models.CharField(max_length=100,choices=PRODUCT_UNIT_STATUS_CHOICES, verbose_name='Status', default='Active')

    product_unit_added_by = models.CharField(verbose_name='Unit Added Added By', blank=True, default='Admin', max_length=100)
    product_unit_added_time = models.DateTimeField(verbose_name='Unit Added Time', auto_now_add=True)

    product_unit_updated_by = models.CharField(verbose_name='Unit Updated By', blank=True, default='Admin', max_length=100)
    product_unit_updated_time = models.DateTimeField(verbose_name='Unit Update Time', auto_now=True)

    def __str__(self):
        return '%s' % (self.product_unit_name,)

    class Meta:
        ordering = ['product_unit_name']
        verbose_name = 'Product Unit'
        verbose_name_plural = 'Product Units'


class Brand(models.Model):

    BRAND_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )


    brand_name = models.CharField(max_length=100, verbose_name='Brand Name', unique=True)
    brand_status = models.CharField(max_length=100,choices=BRAND_STATUS_CHOICES, verbose_name='Status',default='Active')


    brand_added_by = models.CharField(verbose_name='Brand Added Added By', blank=True, default='Admin', max_length=100)
    brand_added_time = models.DateTimeField(verbose_name='Brand Added Time', auto_now_add=True)

    brand_updated_by = models.CharField(verbose_name='Brand Updated By', blank=True, default='Admin', max_length=100)
    brand_updated_time = models.DateTimeField(verbose_name='Brand Update Time', auto_now=True)

    def __str__(self):
        return '%s' % (self.brand_name,)

    class Meta:
        ordering = ['brand_name']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Category(models.Model):

    CATEGORY_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )


    category_name = models.CharField(max_length=100, verbose_name='Category Name',unique=True)
    category_status = models.CharField(max_length=100,choices=CATEGORY_STATUS_CHOICES, verbose_name='Status', default='Active')

    category_description = models.TextField(verbose_name='Description', blank=True)
    category_featured = models.BooleanField(verbose_name='Featured', default=False, null=True, blank=True)

    category_added_by = models.CharField(verbose_name='Category Added Added By', blank=True, default='Admin', max_length=100)
    category_added_time = models.DateTimeField(verbose_name='Category Added Time', auto_now_add=True)

    category_updated_by = models.CharField(verbose_name='Category Updated By', blank=True, default='Admin', max_length=100)
    category_updated_time = models.DateTimeField(verbose_name='Category Update Time', auto_now=True)

    def __str__(self):
        return '%s' % (self.category_name,)

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory_Attached(models.Model):

    category = models.ForeignKey(Category)
    product = models.ForeignKey(Product)

    subcategory_attached = models.ForeignKey('SubCategory', null=True,blank=True, verbose_name='Associated Subcategory')



class SubCategory(models.Model):

    SUB_CATEGORY_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )
    subcategory_name = models.CharField(max_length=100, verbose_name='subcategory Name',unique=True)
    category = models.ForeignKey('Category')
    subcategory_status = models.CharField(max_length=100,choices=SUB_CATEGORY_STATUS_CHOICES, verbose_name='Status', default='Active')

    subcategory_description = models.TextField(verbose_name='Description', blank=True)

    subcategory_added_by = models.CharField(verbose_name='subcategory Added Added By', blank=True, default='Admin', max_length=100)
    subcategory_added_time = models.DateTimeField(verbose_name='subcategory Added Time', auto_now_add=True)

    subcategory_updated_by = models.CharField(verbose_name='subcategory Updated By', blank=True, default='Admin', max_length=100)
    subcategory_updated_time = models.DateTimeField(verbose_name='subcategory Update Time', auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.category,self.subcategory_name,)

    class Meta:
        ordering = ['category__category_name']
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'