# 🍽️ سیستم مدیریت منو هوشمند کافه و رستوران (DGMenu)

## 📋 معرفی پروژه

**DGMenu** یک سیستم مدیریت منو هوشمند برای کافه‌ها و رستوران‌ها است که به مدیران امکان مدیریت کامل منو، اطلاعات کافه و تعامل با مشتریان را می‌دهد. این سیستم شامل پنل مدیریتی برای مدیر اصلی و پنل‌های شخصی برای هر کافه/رستوران می‌باشد.

## ✨ ویژگی‌های اصلی

### 🏢 پنل مدیر اصلی
- مدیریت کلیه کافه‌ها و رستوران‌ها
- نظارت بر عملکرد سیستم
- مدیریت کاربران و نقش‌ها
- گزارش‌گیری جامع

### 🏪 پنل مدیر کافه/رستوران
- مدیریت منوی غذاها و دسته‌بندی‌ها
- آپلود تصاویر و گالری
- مدیریت اطلاعات تیم
- تنظیمات شخصی‌سازی کافه
- مدیریت میزها و رزرو

### 👥 پنل کاربران
- مشاهده منوی کافه‌ها
- جستجو و فیلتر غذاها
- مشاهده اطلاعات کافه و تیم
- گالری تصاویر

## 🛠️ تکنولوژی‌های استفاده شده

### Backend
- **Django 3.2.5** - فریم‌ورک اصلی وب
- **Python 3.x** - زبان برنامه‌نویسی
- **SQLite** - پایگاه داده (قابل تغییر به PostgreSQL/MySQL)

### Frontend
- **HTML5/CSS3** - ساختار و استایل
- **JavaScript** - تعامل کاربر
- **Bootstrap** - فریم‌ورک CSS (احتمالی)

### کتابخانه‌های Django
- **django-crispy-forms** - فرم‌های زیبا
- **django-filter** - فیلتر کردن داده‌ها
- **django-mptt** - ساختار درختی
- **django-taggit** - سیستم برچسب‌گذاری
- **djangorestframework** - API REST
- **Pillow** - پردازش تصاویر
- **social-auth-app-django** - احراز هویت اجتماعی

### امنیت
- **cryptography** - رمزنگاری
- **PyJWT** - توکن‌های JWT
- **defusedxml** - امنیت XML

## 📁 ساختار پروژه

```
dgmenu/
├── dgmenu/                    # تنظیمات اصلی Django
├── adminpanel/               # پنل مدیر اصلی
├── dgmenu_cafe/             # مدل‌های کافه
├── dgmenu_food/             # مدیریت غذاها
├── dgmenu_food_category/    # دسته‌بندی غذاها
├── dgmenu_cafe_team/        # مدیریت تیم کافه
├── dgmenu_cafe_gallery/     # گالری تصاویر
├── dgmenu_cafe_about/       # صفحه درباره ما
├── dgmenu_cafe_tabel/       # مدیریت میزها
├── dgmenu_cafe_viewers/     # نمایش‌دهنده کافه
├── dgmenu_account/          # مدیریت حساب‌ها
├── dgmenu_account_role/     # نقش‌های کاربری
├── dgmenu_site_home/        # صفحه اصلی سایت
├── templates/               # قالب‌های HTML
├── static_cdn/              # فایل‌های استاتیک
└── assets/                  # منابع اضافی
```

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.7+
- pip
- virtualenv (توصیه می‌شود)

### مراحل نصب

1. **کلون کردن پروژه**
```bash
git clone [repository-url]
cd dgmenu
```

2. **ایجاد محیط مجازی**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\Scripts\activate     # Windows
```

3. **نصب وابستگی‌ها**
```bash
pip install -r requirements.txt
```

4. **اجرای مایگریشن‌ها**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **ایجاد سوپر یوزر**
```bash
python manage.py createsuperuser
```

6. **اجرای سرور توسعه**
```bash
python manage.py runserver
```

## 🔧 تنظیمات

### متغیرهای محیطی
فایل `.env` را در ریشه پروژه ایجاد کنید:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### تنظیمات پایگاه داده
برای استفاده از PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dgmenu_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 مدل‌های داده

### Cafe
- اطلاعات کامل کافه (نام، آدرس، تماس)
- لوگو و آیکون‌های مختلف
- تصاویر پس‌زمینه صفحات
- تنظیمات SEO و شبکه‌های اجتماعی

### Food & Category
- مدیریت غذاها با تصاویر
- دسته‌بندی‌های چندسطحی
- قیمت‌گذاری و توضیحات

### Team & Gallery
- مدیریت اعضای تیم
- گالری تصاویر کافه

### Tables
- مدیریت میزها و رزرو

## 🔐 سیستم احراز هویت

- احراز هویت چندسطحی (مدیر اصلی، مدیر کافه، کاربر)
- سیستم نقش‌ها و مجوزها
- احراز هویت اجتماعی (Instagram, Facebook)

## 🎨 شخصی‌سازی

هر کافه می‌تواند:
- لوگو و آیکون خود را آپلود کند
- رنگ‌بندی و استایل صفحات را تغییر دهد
- تصاویر پس‌زمینه را سفارشی کند
- اطلاعات تماس و شبکه‌های اجتماعی را مدیریت کند

## 📱 ویژگی‌های موبایل

- طراحی ریسپانسیو
- بهینه‌سازی برای دستگاه‌های موبایل
- آیکون‌های مختلف برای iOS و Android

## 🔍 SEO و بهینه‌سازی

- متاتگ‌های قابل تنظیم
- ساختار URL بهینه
- نقشه سایت XML
- فایل robots.txt

## 📈 گزارش‌گیری

- آمار بازدید
- گزارش فروش
- تحلیل عملکرد کافه‌ها

## 🚀 استقرار (Deployment)

### برای تولید
```bash
# تنظیم DEBUG = False
# تنظیم ALLOWED_HOSTS
# جمع‌آوری فایل‌های استاتیک
python manage.py collectstatic

# استفاده از WSGI server
gunicorn dgmenu.wsgi:application
```

### پشتیبانی از Passenger
فایل `passenger_wsgi.py` برای استقرار روی سرورهای Passenger آماده شده است.

## 📄 لایسنس

این پروژه تحت لایسنس [MIT](LICENSE) منتشر شده است.

## 📞 پشتیبانی

برای سوالات و پشتیبانی:
- وب‌سایت: [hamyarmenu.ir](https://hamyarmenu.ir)

## 🔄 نسخه‌ها

- **نسخه فعلی**: 1.0.0


---


