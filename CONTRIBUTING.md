# راهنمای مشارکت در پروژه DGMenu

## مقدمه

از مشارکت شما در پروژه DGMenu سپاسگزاریم! این راهنما به شما کمک می‌کند تا به راحتی در توسعه این پروژه مشارکت کنید.

## نحوه مشارکت

### 1. گزارش باگ (Bug Report)

اگر باگی پیدا کردید:

1. ابتدا بررسی کنید که آیا این مشکل قبلاً گزارش شده است یا خیر
2. یک Issue جدید ایجاد کنید
3. عنوان واضح و توصیفی انتخاب کنید
4. مراحل بازتولید مشکل را به دقت توضیح دهید
5. اطلاعات سیستم و مرورگر خود را ذکر کنید
6. اگر ممکن است، اسکرین‌شات یا GIF اضافه کنید

### 2. درخواست ویژگی جدید (Feature Request)

برای درخواست ویژگی جدید:

1. ابتدا بررسی کنید که آیا این ویژگی قبلاً درخواست شده است
2. یک Issue با برچسب "enhancement" ایجاد کنید
3. توضیح دهید که چرا این ویژگی مفید است
4. اگر ممکن است، نمونه‌ای از رابط کاربری یا عملکرد مورد نظر ارائه دهید

### 3. ارسال کد (Code Contribution)

#### مراحل اولیه

1. **Fork کردن پروژه**
   ```bash
   git clone https://github.com/your-username/dgmenu.git
   cd dgmenu
   ```

2. **ایجاد شاخه جدید**
   ```bash
   git checkout -b feature/your-feature-name
   # یا برای رفع باگ
   git checkout -b fix/your-bug-fix
   ```

3. **نصب وابستگی‌ها**
   ```bash
   pip install -r requirements.txt
   ```

4. **اجرای تست‌ها**
   ```bash
   python manage.py test
   ```

#### استانداردهای کدنویسی

- از **PEP 8** برای Python پیروی کنید
- از **نام‌گذاری توصیفی** برای متغیرها و توابع استفاده کنید
- **کامنت‌گذاری مناسب** برای کدهای پیچیده
- **Docstring** برای توابع و کلاس‌ها
- **تست‌نویسی** برای کدهای جدید

#### مثال کد استاندارد

```python
def calculate_total_price(items, tax_rate=0.1):
    """
    محاسبه قیمت کل با در نظر گرفتن مالیات
    
    Args:
        items (list): لیست آیتم‌ها با قیمت
        tax_rate (float): نرخ مالیات (پیش‌فرض: 0.1)
    
    Returns:
        float: قیمت کل شامل مالیات
    """
    subtotal = sum(item['price'] for item in items)
    tax_amount = subtotal * tax_rate
    return subtotal + tax_amount
```

#### Commit کردن تغییرات

از **Conventional Commits** استفاده کنید:

```bash
# برای ویژگی جدید
git commit -m "feat: add user profile management"

# برای رفع باگ
git commit -m "fix: resolve login authentication issue"

# برای بهبود
git commit -m "improve: optimize database queries"

# برای مستندات
git commit -m "docs: update installation guide"
```

#### ارسال Pull Request

1. **Push کردن شاخه**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **ایجاد Pull Request**
   - عنوان واضح و توصیفی
   - توضیح کامل تغییرات
   - لینک به Issue مربوطه (اگر وجود دارد)
   - اسکرین‌شات (برای تغییرات UI)

3. **قالب Pull Request**
   ```markdown
   ## توضیحات
   توضیح مختصر تغییرات انجام شده

   ## نوع تغییر
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## تست‌ها
   - [ ] تست‌های موجود همچنان موفق هستند
   - [ ] تست‌های جدید اضافه شده‌اند
   - [ ] تست‌های دستی انجام شده‌اند

   ## چک‌لیست
   - [ ] کد از استانداردهای PEP 8 پیروی می‌کند
   - [ ] کامنت‌های مناسب اضافه شده‌اند
   - [ ] مستندات به‌روزرسانی شده‌اند
   - [ ] CHANGELOG.md به‌روزرسانی شده است
   ```

## ساختار پروژه

### اپلیکیشن‌های Django

- `dgmenu_cafe/` - مدیریت کافه‌ها
- `dgmenu_food/` - مدیریت غذاها
- `dgmenu_account/` - مدیریت حساب‌ها
- `adminpanel/` - پنل مدیر اصلی

### فایل‌های مهم

- `settings.py` - تنظیمات اصلی
- `urls.py` - مسیریابی
- `models.py` - مدل‌های داده
- `views.py` - منطق کسب‌وکار
- `templates/` - قالب‌های HTML

## تست‌نویسی

### اجرای تست‌ها

```bash
# اجرای تمام تست‌ها
python manage.py test

# اجرای تست‌های یک اپ خاص
python manage.py test dgmenu_cafe

# اجرای تست خاص
python manage.py test dgmenu_cafe.tests.CafeModelTest
```

### نوشتن تست جدید

```python
from django.test import TestCase
from dgmenu_cafe.models import Cafe

class CafeModelTest(TestCase):
    def setUp(self):
        """تنظیمات اولیه برای تست"""
        self.cafe = Cafe.objects.create(
            Cafe_Name="کافه تست",
            Cafe_UserName="test_cafe"
        )
    
    def test_cafe_creation(self):
        """تست ایجاد کافه"""
        self.assertEqual(self.cafe.Cafe_Name, "کافه تست")
        self.assertTrue(self.cafe.Cafe_UserName)
```

## مستندات

### به‌روزرسانی README

- تغییرات مهم را در README.md منعکس کنید
- دستورالعمل‌های نصب را به‌روزرسانی کنید
- مثال‌های جدید اضافه کنید

### به‌روزرسانی CHANGELOG

```markdown
## [Unreleased]

### Added
- ویژگی جدید شما

### Fixed
- رفع باگ شما
```

## مسائل امنیتی

اگر مشکل امنیتی پیدا کردید:

1. **مستقیماً ایمیل بزنید** به [security@hamyarmenu.ir]
2. **جزئیات کامل** مشکل را ارائه دهید
3. **تا زمان رفع مشکل** آن را عمومی نکنید

## سوالات و پشتیبانی

- **Issues**: برای سوالات عمومی
- **Discussions**: برای بحث‌های طولانی‌تر
- **Email**: برای مسائل خصوصی

## قدردانی

از تمام مشارکت‌کنندگان که در بهبود این پروژه کمک می‌کنند، سپاسگزاریم!

---

**نکته**: این راهنما به طور مداوم به‌روزرسانی می‌شود. لطفاً قبل از مشارکت، آخرین نسخه آن را بررسی کنید. 