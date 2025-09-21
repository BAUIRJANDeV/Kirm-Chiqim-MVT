# 💰 Kirim–Chiqim Hisoboti (Django DRF + MVT)

Bu loyiha foydalanuvchiga kirim va xarajatlarini hisoblash, kuzatish va tahlil qilish imkonini beradi.  
Loyihada   **MVT (Template)** qismi mavjud.

---

## ✨ Asosiy imkoniyatlar

- ✅ Kirim va xarajatlarni qo‘shish, yangilash, o‘chirish
- ✅ Sana oralig‘ida filter qilish
- ✅ Kategoriya va to‘lov usuli bo‘yicha hisobotlar

- 
- ✅ MVT (HTML + CSS) interfeys (foydalanuvchi ko‘rishi uchun)

---

## 🛠 Texnologiyalar

- **Backend**: Django 5, Django Rest Framework  
- **Database**: SQLite (default), lekin PostgreSQL yoki MySQL qo‘shish mumkin  
- **Frontend (MVT)**: HTML + CSS (template rendering)  
- **Dokumentatsiya**: drf-yasg (Swagger, ReDoc)  

---

## ⚙️ O‘rnatish

1. Loyihani yuklab oling:
   ```bash
   git clone https://github.com/username/kirim-chiqim.git
   cd kirim-chiqim
Virtual environment yarating va faollashtiring:

bash
Копировать код
python -m venv .env
source .env/bin/activate   # Linux/Mac
.env\Scripts\activate      # Windows
Kerakli kutubxonalarni o‘rnating:

bash
Копировать код
pip install -r requirements.txt
Migratsiyalarni bajaring:

bash
Копировать код
python manage.py migrate
Superuser yarating:

bash
Копировать код
python manage.py createsuperuser
Serverni ishga tushiring:

bash
Копировать код
python manage.py runserver
🔗 API yo‘llari
/api/kirim/ → Kirim CRUD

/api/xarajat/ → Xarajat CRUD

/api/hisobot/kategoriya/ → Kategoriya bo‘yicha hisobot

/api/hisobot/tolov-usuli/ → To‘lov usuli bo‘yicha hisobot

/api/hisobot/balans/ → Balans tarixi

Swagger/Redoc:

/swagger/

/redoc/

🖥 MVT (Interfeys) yo‘llari
/ → Asosiy sahifa (umumiy balans)

/kirim/ → Kirim qo‘shish

/rashod/ → Xarajat qo‘shish

/apiratsya/ → Apiratsiyalar tarixi

/kalendar/ → Kalendar ko‘rinishi

/kategoriya-grafigi/ → Kategoriya bo‘yicha grafik

/tolov-usuli-grafigi/ → To‘lov usuli bo‘yicha grafik

📊 Misol API chiqishi
Balans tarixi:

json
Копировать код
[
  {"sana": "2025-09-01", "balans": 10000},
  {"sana": "2025-09-02", "balans": 15000},
  {"sana": "2025-09-03", "balans": 12000}
]
Kategoriya bo‘yicha hisobot:

json
Копировать код
{
  "Oziq-ovqat": 150000,
  "Transport": 80000,
  "Kiyim-kechak": 50000
}
👨‍💻 Muallif
Ism: Bauirjan Mamataliv

Loyiha: Backend (Python + Django + DRF) kurs doirasida yaratilgan

yaml
Копировать код
