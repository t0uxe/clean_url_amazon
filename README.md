# 🚀 Amazon URL Cleaner - Terminal Edition

## 📌 Overview

Amazon URL Cleaner is a **Python script** designed to remove tracking parameters from Amazon product URLs, leaving only the essential part. It helps you get **clean and shareable Amazon links** without unnecessary data.

---

## 🎯 Features

✅ Removes tracking parameters from Amazon URLs.\
✅ Works with different Amazon domains (e.g., `.es`, `.com`, `.de`).\
✅ Checks if the URL is accessible before cleaning.\
✅ Prevents invalid URLs from being processed.\
✅ Handles user interruptions (`Ctrl+C`) gracefully.\
✅ Simulates a real browser to bypass Amazon's bot protection.

---

## 🛠 Installation & Usage

### 🔽 Prerequisites

Make sure you have Python installed (Python 3 recommended). If not, install it:

```bash
sudo apt update && sudo apt install python3
```

### 🔧 Install Required Packages

The script uses the `requests` module. Install it with:

```bash
pip install requests
```

### 🚀 Run the Script

1. **Download or clone the repository:**

   ```bash
   git clone https://github.com/YOUR-USERNAME/amazon-url-cleaner.git
   cd amazon-url-cleaner
   ```

2. **Give execution permissions:**

   ```bash
   chmod +x amazon_cleaner.py
   ```

3. **Run the script:**

   ```bash
   ./amazon_cleaner.py
   ```

   Or using Python directly:

   ```bash
   python amazon_cleaner.py
   ```

---

## 📷 Example Usage

```bash
==================================================
🚀 Amazon URL Cleaner - Terminal Edition 🚀
==================================================
🔗 Enter Amazon URL: https://www.amazon.es/Mazomorra-Dungeon-ESPA%C3%91OL-Solitario-Jugadores/dp/B0DMT5SFWJ?tag=tracking123
🛠 Debug: Parsed URL -> Scheme: https, Netloc: www.amazon.es
🔍 Checking if the URL exists...
🛠 Debug: HTTP Status Code: 200
✅ Cleaned Amazon URL: https://www.amazon.es/dp/B0DMT5SFWJ
```

---

## ⚙️ How It Works

1. **Asks for an Amazon URL** and validates it.
2. **Checks if the URL is accessible** (avoiding invalid links).
3. **Extracts the ASIN (Amazon product code)**.
4. **Reconstructs the clean URL** in the format:
   `https://www.amazon.[domain]/dp/ASIN`
5. **Displays the cleaned URL** in a readable format.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or contribute to the repository.

---

## ⭐ Support

If you find this project useful, **give it a star ⭐ on GitHub!** 🚀


