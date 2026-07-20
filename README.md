# Xarajatlar Kundaligi API

Bu shaxsiy xarajatlarni hisob-kitob qilib borish uchun Django REST Framework orqali yozilgan backend loyihasi.

## Texnologiyalar
* Django
* Django REST Framework
* SQLite (yoki PostgreSQL)

---

## Qanday o'rnatish va ishga tushirish

1. Virtual muhit ochib, kerakli kutubxonalarni yuklab olasiz:
```bash
python -m venv venv
source venv/Scripts/activate  

2. Migratiya qilish

python manage.py makemigrations
python manage.py migrate

3. Serverni ishga tushirish

python manage.py runserver