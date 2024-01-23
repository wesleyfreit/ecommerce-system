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

**8. Access swagger docummentation:**
```bash
{{baseUrl}}/docs
``` 

## 🌐 Quick Start Deploy AWS EB

#### Requirements: AWS Account, PG Serverless DB, AWS CLI, EB CLI

---

**1. Install and set the path for AWS CLI and EB CLI.**

**2. Create an user to get access to AWS resources on AWS IAM page.**

**3. Set the AWS CLI config with the access key and access token received on the AWS CLI page with this command:**

```bash
aws configure
```

**4. In the project directory, run this command to create an EB App.**

```bash
eb init -p python-3.11 ecommerce-system  --region us-east-1
```

**5. Run this command to upload and deploy the ambient:**

```bash
eb create ecommerce-system-api
```

**6. Now, on the ecommerce-system EB ambient page, set the project environment variables.**

---
### ➕ Extra

**To update and redeploy the code, be sure to commit it and then run this:**

```bash
eb deploy ecommerce-system-api
```

**To terminate and delete the ambient, run this:**

```bash
eb delete-app ecommerce-system-api
```

**To view eb deploy logs:**

```bash
eb logs ecommerce-system-api
```