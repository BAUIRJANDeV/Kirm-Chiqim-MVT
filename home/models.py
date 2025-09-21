from django.db import models

class Xarajat(models.Model):
    miqdor = models.DecimalField(max_digits=12, decimal_places=2)
    kategoriya = models.CharField(max_length=50)
    tolov_usuli = models.CharField(max_length=50)
    izoh = models.TextField(blank=True, null=True)
    sana = models.DateField()
    vaqt = models.TimeField(blank=True, null=True)
    takroriymi = models.BooleanField(default=False)
    eslatma = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.sana} - {self.miqdor} so‘m ({self.kategoriya})"



class Kirim(models.Model):
    miqdor = models.DecimalField(max_digits=12, decimal_places=2)
    kategoriya = models.CharField(max_length=50)
    tolov_usuli = models.CharField(max_length=50)
    izoh = models.TextField(blank=True, null=True)
    sana = models.DateField()
    vaqt = models.TimeField(blank=True, null=True)
    takroriymi = models.BooleanField(default=False)
    eslatma = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.sana} - {self.miqdor} so‘m ({self.kategoriya})"

