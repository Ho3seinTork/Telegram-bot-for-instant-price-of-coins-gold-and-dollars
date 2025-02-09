# Telegram Price Bot | ربات قیمت طلا و سکه در تلگرام

This bot retrieves and sends real-time gold and coin prices from an API using Telegram.

این ربات قیمت لحظه‌ای طلا و سکه را از یک API دریافت کرده و در تلگرام ارسال می‌کند.

---

## How It Works | نحوه کارکرد

- The bot fetches the latest prices from `https://price.tlyn.ir/api/v1/price`.
- It displays buttons for different price categories (Gold Gram 18K, Mithqal 17K, Full Coin, etc.).
- When a button is pressed, the bot retrieves the relevant price, converts it to Toman (×1000), and sends it to the user.

- ربات قیمت‌های لحظه‌ای را از `https://price.tlyn.ir/api/v1/price` دریافت می‌کند.
- دکمه‌هایی برای دسته‌بندی‌های مختلف قیمت (طلا 18 عیار، مثقال 17 عیار، سکه کامل و...) نمایش می‌دهد.
- با انتخاب هر دکمه، قیمت مربوطه را دریافت کرده، به تومان (×1000) تبدیل می‌کند و برای کاربر ارسال می‌کند.

---

## Commands | دستورات

- `/start` → Displays the menu with price options.
- `[Gold Gram 18K]` → Shows the current sell/buy price of 18K gold per gram.
- `[Mithqal 17K]` → Shows the current sell/buy price of 17K gold per mithqal.
- `[Full Coin]` → Shows the current price of a full gold coin.
- `[Half Coin]` → Shows the current price of a half gold coin.
- `[Quarter Coin]` → Shows the current price of a quarter gold coin.

- `/start` → نمایش منو با گزینه‌های قیمت‌گذاری
- `[طلا 18 عیار]` → نمایش قیمت خرید/فروش لحظه‌ای طلا 18 عیار به گرم
- `[مثقال 17 عیار]` → نمایش قیمت خرید/فروش مثقال 17 عیار
- `[سکه تمام]` → نمایش قیمت لحظه‌ای سکه تمام
- `[نیم سکه]` → نمایش قیمت لحظه‌ای نیم سکه
- `[ربع سکه]` → نمایش قیمت لحظه‌ای ربع سکه
