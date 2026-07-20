# Xarajatlar Kundaligi API

Bu shaxsiy xarajatlarni hisob-kitob qilib borish uchun Django REST Framework (DRF) orqali yozilgan backend loyihasi.

## Texnologiyalar
* Django
* Django REST Framework
* SQLite (yoki PostgreSQL)

---

## Qanday o'rnatish va ishga tushirish

1. Virtual muhit ochib, kerakli kutubxonalarni yuklab olasiz:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows uchun
# Linux yoki Mac uchun: source venv/bin/activate
pip install -r requirements.txt

Ma'lumotlar bazasini tayyorlash (Migratsiya qilish):

Bash
python manage.py makemigrations
python manage.py migrate