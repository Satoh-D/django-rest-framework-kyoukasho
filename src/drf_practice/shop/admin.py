from django.contrib import admin

from .models import Book

# Register your models here.
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id', 'created_at')   # 固定長リストはtupleで指定するとパフォーマンス○
    ordering = ('-created_at',)                             # 管理画面での表示順序を指定
    readonly_fields = ('id', 'created_at')                  # 編集不可項目の指定


admin.site.register(Book, BookModelAdmin)
