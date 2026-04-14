# استخدم Python خفيف
FROM python:3.11-slim

# مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY . .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل المشروع
CMD ["python", "main.py"]
