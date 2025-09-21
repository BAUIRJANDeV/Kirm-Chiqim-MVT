from django.contrib import admin
from .models import Kirim,Xarajat

from django.contrib import admin
from .models import Kirim,Xarajat

@admin.register(Kirim)
class KirimAdmin(admin.ModelAdmin):
    list_display = ('sana', 'miqdor', 'kategoriya', 'tolov_usuli', 'takroriymi')
    list_filter = ('kategoriya', 'tolov_usuli', 'sana')
    search_fields = ('izoh',)

    def __str__(self):
        return f"{self.sana} - {self.miqdor} so‘m ({self.kategoriya})"



@admin.register(Xarajat)
class XarajatAdmin(admin.ModelAdmin):
    list_display = ("miqdor", "kategoriya", "tolov_usuli", "sana", "vaqt", "takroriymi")
    list_filter = ("kategoriya", "tolov_usuli", "takroriymi", "sana")
    search_fields = ("izoh", "eslatma")
    ordering = ("-sana", "-vaqt")

# Register your models here.
