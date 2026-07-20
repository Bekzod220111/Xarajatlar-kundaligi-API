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

Mi'gratiya qilish:
Bash
python manage.py makemigrations
python manage.py migrate

Serverni ishga tushirish
Bash
python manage.py runserver