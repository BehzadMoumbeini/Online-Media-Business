import os.path

from django.db import models
from django.utils.translation import ugettext_lazy as _


#order of each section: for making the tables 1- fields (class) 2- class meta  3- methods with dunder (____) 4- methods you want to add
class Category(models.Model):
    #it has foreignkey to itself (self), when we have category and sub-category (the ones with null=Trus are parent category)
    #this model is onetoone with Foreginkey (Foreginkey=to one specific record an manytomany =to some specific record)
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

#oneoone = only one specific record

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('categories')

#here we should define a method __str__ which returns title, otherwise if you add a category in the web-browser it will be Category object(1)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    #save the avatar in this directory: products/
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    # blank=True because there might be no category
    #here we make this model manytomany (one product cab belong more than one category) with category model
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


# for example each series can have many files, so better to have a separate class for files
#files will be uploaded here and will be connected to Product
class File(models.Model):
    #should be connected to only one product (so it is foreignkey to Product model). one or some files can belong to one product
    #each product could have one or more than one product
    # each file can be connected to each file one by one
    #related_name='files' --> this name will be shown in browser for the files belong th products
    #for data type, I added below few lines. the ones with capital letters (and int in front of them) will be in DB and with small letter will be shown in browser (admin page)
    #since the admin is "Inline", go to admin.py, and add file_type in FileInlineAdmin  --> fields
    #and line file_type is added below as well. since we have few types I used PositiveSmallIntegerField.
    #also in serializers.py add file_type in FileSerializer. and add a method named: get_file_type (to get the name of type not just a number, 1 or 2 or 3)
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, _('audio')),
        (FILE_VIDEO, _('video')),
        (FILE_PDF, _('pdf'))
    )
    product = models.ForeignKey('Product', verbose_name=_('product'), related_name='files', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES) #default argument can be here but we can chang when add one file in the browser
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    #all the files for the same day will be uploaded to separate sub-directory with specific date
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title

#all the files will be uploaded to one of these 3 folders (products, categories or files)
#but these folders should also be in a directory ==>
#go to settings.py and do the following:
#1- import os (on top of script)
#2- add this at the end --> #Media Files
# 3- add this at the end to put the files here --> MEDIA_ROOT = os.path.join((BASE_DIR, 'media/'))
# 4- add this at the end to show the files here --> MEDIA_URL = 'media/'
