# 🛒 BigBasket Bangladesh Automation Testing

## 📌 Project Overview

This project is a Selenium Automation Testing Framework developed for the BigBasket Bangladesh website.

The framework follows the **Page Object Model (POM)** design pattern and uses **Behavior Driven Development (BDD)** with **Behave** to create maintainable, reusable, and scalable automated test scripts.

This project was developed as a University Automation Testing Lab Project.

---

# 🌐 Website

https://bigbasket.com.bd/

---

# 🚀 Technology Stack

- Python 3.x
- Selenium WebDriver
- Behave (BDD)
- Page Object Model (POM)
- WebDriver Manager
- Explicit Wait
- ConfigParser
- Logging
- Screenshot Utility

---

# 📂 Project Structure

```
BigBasketAutomation/
│
├── config/
├── features/
│   ├── steps/
│   ├── homepage.feature
│   ├── search.feature
│   ├── product.feature
│   ├── cart.feature
│   ├── category.feature
│   ├── login.feature
│   ├── footer.feature
│   └── environment.py
│
├── pages/
├── utils/
├── reports/
├── screenshots/
├── logs/
├── test_data/
│
├── config.ini
├── behave.ini
├── requirements.txt
└── README.md
```

---

# ✅ Automated Test Scenarios

- Homepage Validation
- Product Search
- Product Details Verification
- Add Product to Cart
- Remove Product from Cart
- Category Navigation
- Login Popup Validation
- Footer Validation

---

# ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/sabbir1494/BigBasketAutomation.git
```

Go to Project

```bash
cd BigBasketAutomation
```

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Mac/Linux

```bash
python3 -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Tests

Run All Features

```bash
behave
```

Run Search Feature

```bash
behave features/search.feature
```

Run Homepage Feature

```bash
behave features/homepage.feature
```

---

# 📸 Reports

Reports are generated under

```
reports/
```

---

# 📷 Screenshots

Failed test screenshots are stored inside

```
screenshots/
```

---

# 📝 Logs

Execution logs are stored inside

```
logs/
```

---

# 📖 Framework Design

Feature File

↓

Step Definition

↓

Page Object

↓

Base Page

↓

Utilities

↓

Selenium WebDriver

---

# 👨‍💻 Author

**Sabbir Hossain**

Software Engineering

Daffodil International University

Bangladesh