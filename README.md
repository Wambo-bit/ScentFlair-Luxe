# 🌸 ScentFlair Luxe

**ScentFlair Luxe** is a Django-based e-commerce web application for discovering and purchasing luxury perfumes.  
It offers a seamless shopping experience — from browsing products to placing orders with M-Pesa payment support.

---

## 🚀 Features

- 🛍️ Browse and view perfumes by category or name  
- 🧺 Add products to cart and update quantities  
- 💳 Checkout with user details and M-Pesa payment  
- 🔐 User authentication (register, login, logout)  
- 📦 Track orders and payment status  
- 🧾 Admin panel for managing products, orders, and users  

---

## 🧩 Tech Stack

- **Backend:** Django 5+ (Python 3.13)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default) – easy to switch to PostgreSQL/MySQL
- **Payment Integration:** M-Pesa (manual entry simulation)
- **Version Control:** Git & GitHub

---

## 🗂️ Project Structure

ScentFlair_Luxe/
│
├── accounts/ # Custom user registration & authentication
├── cart/ # Cart, checkout, and payment functionality
├── products/ # Product listings, categories, and details
├── scentflair_luxe/ # Main Django project settings and URLs
├── static/ # CSS, JS, and images
├── templates/ # HTML templates
└── manage.py # Django management script

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Wambo-bit/ScentFlair_Luxe.git
cd ScentFlair_Luxe
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py runserver
Then open your browser and go to:
👉 http://127.0.0.1:8000/
💡 Usage Guide

Register or log in to your account.

Browse perfumes in the shop.

Add items to cart and adjust quantities.

Proceed to checkout — enter your name, phone, and address.

Submit M-Pesa payment details (manual entry for now).

Receive your order confirmation.
🔒 Admin Panel Access

Manage products, users, and orders through the Django admin dashboard.

URL:http://127.0.0.1:8000/admin/
Login using:
The credentials created with createsuperuser.

🛠️ Future Enhancements

🔌 Real M-Pesa API integration

📧 Email order confirmations

⭐ Customer reviews & ratings

📦 Inventory & stock management

👩‍💻 Author

Mary Wambui Muthima
💼 Passionate about web development, design, and user experience.
🔗 GitHub
 | LinkedIn
 

✨ "Luxury in every scent — delivered with elegance." ✨
