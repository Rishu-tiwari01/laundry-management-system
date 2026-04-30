# 🧺 Mini Laundry Order Management System

A simple web-based Laundry Management System built using **Django**. This project helps manage customer orders, track order status, and monitor business performance through a clean dashboard.

---

## 🚀 Features

### ✅ Order Management

* Create new laundry orders
* Auto-generate unique Order ID
* Calculate total bill automatically

### 📊 Dashboard

* Total number of orders
* Total revenue
* Orders categorized by status

### 🔍 Search & Filter

* Search by customer name or phone number
* Filter orders by status:

  * RECEIVED
  * PROCESSING
  * READY
  * DELIVERED

### 🎨 UI

* Responsive design using Bootstrap
* Modern dashboard with cards and tables
* Navigation bar with search functionality

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default)

---

## 📂 Project Structure

```
laundry_project/
│── manage.py
│── laundry_project/
│   ├── settings.py
│   ├── urls.py
│
│── orders/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── create_order.html
│       ├── orders_list.html
```

---

## ⚙️ Installation & Setup

### 1. Clone Project / Create Environment

```bash
pip install django
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Start Server

```bash
python manage.py runserver
```

### 4. Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

* When a new order is created:

  * A unique **Order ID** is generated
  * **Total bill = Quantity × Price per item**
* Dashboard dynamically updates:

  * Total orders
  * Revenue
  * Status breakdown

---

## 📌 Future Improvements

* User authentication (Login/Logout)
* Admin panel customization
* Order edit & delete functionality
* Charts (Chart.js) for analytics
* SMS/Email notification system

---

## 👨‍💻 Author

**Rishu Tiwari**
Beginner Django Developer 🚀

---

## 📄 License

This project is for educational purposes only.
