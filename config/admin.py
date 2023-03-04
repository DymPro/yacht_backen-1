from django.contrib import admin
from config.models import *
# Register your models here.

class ExtraFieldsInline(admin.TabularInline):
    model = ExtraFields
    extra = 0


@admin.register(CardFields)
class CardFieldsAdmin(admin.ModelAdmin):
    inlines = [ExtraFieldsInline,]


class CardFieldsInline(admin.TabularInline):
    model = CardFields
    extra = 0
    show_change_link = True


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['title','sort_order']
    list_editable = ['sort_order']
    inlines = [CardFieldsInline,]

@admin.register(Tabs)
class TabsAdmin(admin.ModelAdmin):
    list_display = ['title','sort_order']
    list_editable = ['sort_order']

class TabsInline(admin.TabularInline):
    model = Tabs
    extra = 0

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['title','sort_order']
    list_editable = ['sort_order']
    inlines = [TabsInline,]
