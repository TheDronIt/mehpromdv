from django.contrib import admin
from .models import News, Message, Product
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'        

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(News, NewsAdmin)
admin.site.register(Message)
admin.site.register(Product, ProductAdmin)
# Register your models here.
