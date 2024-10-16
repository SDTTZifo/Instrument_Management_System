# Instrument Management System - SDTT

The Instrument Management System is designed to streamline the organization and management of various instruments. This README provides a step-by-step guide to help you configure and run the application on your local machine.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Configuration Steps](#configuration-steps)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Create Environment](#step-2-create-environment)
   - [Step 3: Activate Environment](#step-3-activate-environment)
   - [Step 4: Install Required References](#step-4-install-required-references)
   - [Step 5: Run the Python Program](#step-5-run-the-python-program)
3. [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.x
- Git

## Configuration Steps

### Step 1: Clone the Repository

To get a local copy of the project, you need to clone it using Git. This will create a directory named `Instrument_Management_System` on your machine.

```bash
git clone https://github.com/SDTTZifo/Instrument_Management_System.git
```
##### Username :
```text
SDTTZifo 
```
##### Private Key :
```text
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
```

### Step 2: Create Environment

It is recommended to create a virtual environment to manage dependencies for this project. You can create a virtual environment using the following command:
```bash
cd Instrument_Management_System
```

- On Windows:
  ```bash
  python -m venv env
  
- On macOS/Linux:
  ```bash
  python3 -m venv env
  ```

### Step 3: Activate Environment

Once the virtual environment is created, activate it using:

- On Windows:
  ```bash
  .\env\Scripts\activate
  
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### Step 4: Install Required References

With your virtual environment activated, install the required packages listed in `requirements.txt`:

```bash
pip install -r Requirements.txt
```

### Step 5: Run the Python Program

After installing all dependencies, you can run the application using:

- On Windows:
  ```bash
  py .\manage.py runserver
  
- On macOS/Linux:
  ```bash
  python3 manage.py runserver
  ```
   #### 5.1. Create a Superuser (Optional)
   
   If you need to create a superuser to access the Django admin, run:
   
   ```bash
   python manage.py createsuperuser
   ```
   ### 5.2. Access the Django Admin

   To log in to the Django admin, use the following credentials:
   
   - **Username:**
     
      ```text
      admin
      ```
   - **Password:**
     
       ```text
       Password@123
       ```
   
  Navigate to below URL to access the admin panel.
  
  ```url
  http://localhost:8000/admin
  ```

## Contributing

Fellow Zifoites! 

We welcome contributions from everyone! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.
