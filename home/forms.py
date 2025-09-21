from django import forms
from django.db.transaction import clean_savepoints

from .models import Kirim,Xarajat

class KirimForm(forms.ModelForm):
    class Meta:
        model = Kirim
        fields = ['miqdor', 'kategoriya', 'tolov_usuli', 'izoh', 'sana', 'vaqt', 'takroriymi', 'eslatma']


class XarajatForm(forms.ModelForm):
    class Meta:
        model=Xarajat
        fields=['miqdor', 'kategoriya', 'tolov_usuli', 'izoh', 'sana', 'vaqt', 'takroriymi', 'eslatma']