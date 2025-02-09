# Telegram-bot-for-instant-price-of-coins-gold-and-dollars
ربات قیمت دلار، سکه و طلا در بات تلگرام
این پروژه یک بات تلگرام ساده است که با دریافت اطلاعات از یک API قیمت‌های به‌روز طلا و سکه‌های مرتبط (مانند طلا 18 عیار، مثقال 17 عیار، سکه کامل/نیمه/ربع) را ارسال می‌کند. این ربات با زبان پایتون نوشته شده و از کتابخانه‌های requests و pyTelegramBotAPI استفاده می‌کند.

ویژگی‌ها:
دریافت قیمت به‌روز: دریافت قیمت‌های جدید انواع طلا (مانند Gold Gram 18K، Mithqal 17K، سکه کامل، نیمه و ربع).
رابط کاربری با کیبورد سفارشی: ارائه دکمه‌های پیش‌فرض برای انتخاب هر نوع قیمت.
راه‌اندازی آسان: کافیست توکن ربات تلگرام خود را جایگزین کنید و اسکریپت را اجرا نمایید.
نصب
کلون کردن مخزن:
bash
Copy
Edit
git clone https://github.com/yourusername/telegram-price-bot.git
cd telegram-price-bot
نصب پکیج‌های مورد نیاز:
bash
Copy
Edit
pip install requests
pip install pyTelegramBotAPI
ایجاد ربات تلگرام:
با استفاده از BotFather در تلگرام یک ربات جدید بسازید و توکن API آن را دریافت کنید.
تنظیمات:
فایل bot.py را باز کنید.
مقدار 'YOUR_API_TOKEN_HERE' را با توکن واقعی ربات خود جایگزین کنید.
اجرای ربات:
bash
Copy
Edit
python bot.py
در تلگرام با ربات خود چت را آغاز کرده و دستور /start را ارسال کنید.
نحوه کارکرد
ربات با ارسال یک درخواست HTTP GET به آدرس https://price.tlyn.ir/api/v1/price، قیمت‌های به‌روز را دریافت می‌کند.
دکمه‌های از پیش تعریف شده (مانند "Gold Gram 18K"، "Mithqal 17K"، و ...) برای انتخاب توسط کاربر نمایش داده می‌شود.
زمانی که کاربر یکی از دکمه‌ها را انتخاب می‌کند، ربات قیمت مربوطه را پیدا کرده، آن را به تومان (ضرب در 1000) تبدیل می‌کند و نتیجه را به کاربر ارسال می‌کند.
مجوز
این پروژه به صورت متن‌باز تحت مجوز MIT منتشر شده است.

yaml
Copy
Edit

---

You can save the above content as `README.md` in your repository. Adjust the repository URL and any specific details (like the list of buttons or API endpoint) as necessary.






