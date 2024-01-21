## 💻 Project

### 📖 Title
**ecommerce-system**

### 📝 Description
**A simple Ecommerce System API built using Python fundamentals**

## 🚀 Quick Start

#### Requirements: Python3, PostgreeSQL

---

**1. Create a virtual environment:**
```bash
py -m venv .venv
```

**2. Close the current terminal and open another.**

**3. Install the project dependencies:**

```bash
pip3 install -r requirements.txt  
```

**4. Create a `.env` file in the API project root folder with the following variables:**

```bash
DATABASE_URL = postgresql://user:password@localhost:5432/mydatabasename
SECRET_KEY = @secret-key
USER = admin_username
PASSWORD = @Admin_p4ssword
```

**5. Persist models in the database:**

```bash
py src/_persist.py
```

**6. Persist migration in the database:**

```bash
py src/_migration.py
```

**7. Run the project:**

```bash
py src/app.py  
```
