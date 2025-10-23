# 🔗 URL Shortener

A simple and powerful URL shortener built using **Python Django**.  
It converts long URLs into short, shareable links, tracks visit counts, and generates **QR codes** automatically.

---

## 🚀 Features

- ✨ Shorten long URLs instantly  
- 🔁 Redirect to the original link automatically  
- 📊 Track how many times each link was used  
- 🧾 Display the last 5 shortened URLs  
- 📱 Generate QR codes for easy mobile scanning  
- 💅 Clean, modern, and responsive interface  
- ⚡ Built with Django, HTML, CSS, and Bootstrap  

---

## 🧠 How It Works

1. User enters a long URL in the text box.  
2. The system creates a **unique short code**.  
3. The shortened link redirects to the original URL.  
4. Visit counts are stored and displayed.  
5. A QR code is generated for each short link.  

---

## 🧩 Technologies Used

| Category  |        Tools         |
|-----------|----------------------|
| Backend   | Python, Django       |
| Frontend  | HTML, CSS, Bootstrap |
| Database  | SQLite               |
| Libraries | qrcode, pillow       |

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/django-url-shortener.git
cd django-url-shortener
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
## If you don’t have a requirements.txt file yet, run:
pip install django qrcode pillow
pip freeze > requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the server
```bash
python manage.py runserver
```
### Then open your browser and visit 👉 http://127.0.0.1:8000/

## 🧑‍💻 Usage
- Enter a long URL (like https://example.com/very/long/path)
- Click Shorten URL
- Copy or scan the generated short link / QR code
- See visit counts update automatically


