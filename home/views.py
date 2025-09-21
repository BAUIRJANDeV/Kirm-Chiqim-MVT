from calendar import monthrange
from datetime import date

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Kirim,Xarajat
from .forms import KirimForm,XarajatForm


def home_page(request):
    xarajat=Xarajat.objects.all().order_by('-sana','-vaqt')[:2]
    kirimlar = Kirim.objects.all().order_by('-sana','-vaqt')[:2]
    total=Kirim.objects.aggregate(Sum("miqdor"))["miqdor__sum"] or 0
    xarajat_total=Xarajat.objects.aggregate(Sum("miqdor"))["miqdor__sum"] or 0
    balans= sum([i.miqdor for i in Kirim.objects.all()])-sum([i.miqdor for i in Xarajat.objects.all()])
    dolor=balans/1250000
    return render(request, 'inbox.html', {'kirimlar': kirimlar,'total':total,'xarajat_total':xarajat_total,'balans':balans,'xarajat':xarajat,"dolor":dolor})



def kirim_qoshish(request):
    if request.method == "POST":
        forma = KirimForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('home')
        else:
            print("Forma valid emas:", forma.errors)
    else:
        forma = KirimForm()
    return render(request, 'kirim.html', {'forma': forma})


def xarajat_qoshish(request):
    if request.method=="POST":
        forma=XarajatForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('home')
    else:
        forma = XarajatForm()
    return render(request, 'rashod.html', {'forma': forma})

def apiratsyalar_page(request):
    xarajat = Xarajat.objects.all().order_by('-vaqt')
    kirimlar = Kirim.objects.all().order_by('-sana')
    total=kirimlar.aggregate(Sum("miqdor"))["miqdor__sum"] or 0
    xarajat_total=xarajat.aggregate(Sum("miqdor"))["miqdor__sum"] or 0
    balans= sum([i.miqdor for i in Kirim.objects.all()])-sum([i.miqdor for i in Xarajat.objects.all()])
    return render(request,'apiratsyalar.html',{'kirimlar': kirimlar,'total':total,'xarajat':xarajat,'xarajat_total':xarajat_total,'balans':balans})


def kalendar_page(request):
    today = date.today()
    current_year = today.year
    current_month = today.month
    num_days = monthrange(current_year, current_month)[1]


    month_days = [date(current_year, current_month, d) for d in range(1, num_days + 1)]


    daily_data = []
    for d in month_days:
        kirimlar = Kirim.objects.filter(sana=d)
        xarajatlar = Xarajat.objects.filter(sana=d)
        total_kirim = kirimlar.aggregate(Sum('miqdor'))['miqdor__sum'] or 0
        total_xarajat = xarajatlar.aggregate(Sum('miqdor'))['miqdor__sum'] or 0
        daily_data.append({
            "day": d,
            "total_kirim": total_kirim,
            "total_xarajat": total_xarajat
        })

    context = {
        "current_month": today.strftime("%B"),
        "current_year": current_year,
        "daily_data": daily_data,
    }

    return render(request, 'kalendar.html', context)

def kategoriya_grafik(request):
    xarajatlar = Xarajat.objects.values('kategoriya').annotate(total=Sum('miqdor'))
    kirimlar = Kirim.objects.values('kategoriya').annotate(total=Sum('miqdor'))

    xarajat_labels = [x['kategoriya'].capitalize() for x in xarajatlar]
    xarajat_data = [float(x['total']) for x in xarajatlar]

    kirim_labels = [k['kategoriya'].capitalize() for k in kirimlar]
    kirim_data = [float(k['total']) for k in kirimlar]

    context = {
        'xarajat_labels': xarajat_labels,
        'xarajat_data': xarajat_data,
        'kirim_labels': kirim_labels,
        'kirim_data': kirim_data,
    }

    return render(request, 'kategoriya_grafik.html', context)





def tolov_usuli_grafik(request):
    kirim_tolov = Kirim.objects.values('tolov_usuli').annotate(total=Sum('miqdor'))
    xarajat_tolov = Xarajat.objects.values('tolov_usuli').annotate(total=Sum('miqdor'))

    kirim_labels = [k['tolov_usuli'] for k in kirim_tolov]
    kirim_data = [float(k['total']) for k in kirim_tolov]

    xarajat_labels = [x['tolov_usuli'] for x in xarajat_tolov]
    xarajat_data = [float(x['total']) for x in xarajat_tolov]

    context = {
        "kirim_labels": kirim_labels,
        "kirim_data": kirim_data,
        "xarajat_labels": xarajat_labels,
        "xarajat_data": xarajat_data,
    }
    return render(request, "tolov_usuli_grafigi.html", context)

def kirim_detail(request, pk):
    kirim = get_object_or_404(Kirim, pk=pk)
    return render(request, 'kirim_detail.html', {'kirim': kirim})

def xarajat_detail(request, pk):
    chiqim = get_object_or_404(Xarajat, pk=pk)
    return render(request, 'xarajat_detail.html', {'xarajat': chiqim})

def kirim_update(request, pk):
    kirim = get_object_or_404(Kirim, pk=pk)
    if request.method == "POST":
        forma = KirimForm(request.POST, instance=kirim)
        if forma.is_valid():
            forma.save()
            return redirect('kirim_detail', pk=kirim.pk)  # o‘sha sahifaga qaytadi
    else:
        forma = KirimForm(instance=kirim)
    return render(request, 'kirim_update.html', {'forma': forma, 'kirim': kirim})


def kirim_delete(request, pk):
    kirim=get_object_or_404(Kirim,pk=pk)
    if request.method=="POST":
        kirim.delete()
        return redirect('apiratsya')
    return render(request, "kirim_delete_confirm.html", {"kirim": kirim})



def xarajat_delete(request,pk):
    xarajat=get_object_or_404(Xarajat,pk=pk)
    if request.method=="POST":
        xarajat.delete()
        return redirect('apiratsya')
    return render(request,'xarajat_delete_confirm.html',{'xarajat':xarajat})



def xarajat_update(request, pk):
    xarajat = get_object_or_404(Xarajat, pk=pk)
    if request.method == "POST":
        forma = XarajatForm(request.POST, instance=xarajat)
        if forma.is_valid():
            forma.save()
            return redirect('kirim_detail', pk=xarajat.pk)
    else:
        forma = KirimForm(instance=xarajat)
    return render(request, 'xarajat_update.html', {'forma': forma, 'xarajat': xarajat})





def tolov_usuli(request):
    usul = request.GET.get("usul")
    yozuvlar = []

    if usul:
        # Kirimlarni olish
        kirimlar = Kirim.objects.filter(tolov_usuli__iexact=usul).values("sana", "miqdor")
        for k in kirimlar:
            yozuvlar.append({
                "sana": k["sana"],
                "turi": "Kirim",
                "miqdor": k["miqdor"]
            })

        # Xarajatlarni olish
        xarajatlar = Xarajat.objects.filter(tolov_usuli__iexact=usul).values("sana", "miqdor")
        for x in xarajatlar:
            yozuvlar.append({
                "sana": x["sana"],
                "turi": "Xarajat",
                "miqdor": x["miqdor"]
            })

    context = {
        "yozuvlar": yozuvlar,
        "tanlangan_usul": usul
    }
    return render(request, "tolov_usuli.html", context)