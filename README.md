# 🎓 PSUSphere  

## 📋 Description  
PSUSphere is a web‑based student organization management system built using the **Django** framework. It is designed for **Palawan State University (PSU)** to streamline the management of student organizations, memberships, academic programs, and colleges. The system provides an intuitive **admin interface** that allows administrators to efficiently manage and monitor all student‑organization‑related data in one centralized platform.  

---

## ✨ Features  

- 🏫 **College Management** – Add, update, and manage colleges within the university  
- 📚 **Program Management** – Track academic programs and their associated colleges  
- 🏢 **Organization Management** – Create and manage student organizations with descriptions and college affiliations  
- 👨‍🎓 **Student Management** – Register students with their personal information and academic program  
- 🤝 **Membership Tracking** – Monitor which students belong to which organizations and when they joined  
- 🔍 **Search & Filter** – Easily search and filter records through the Django Admin interface  
- 🤖 **Automated Data Generation** – Uses the **Faker** library to generate realistic fake data for testing purposes  
- 🔐 **Secure Admin Access** – Protected admin panel with superuser authentication  

---

## 🛠️ Technologies Used
- **Python** – Core programming language
- **Django** – High-level Python web framework
- **SQLite** – Default lightweight database for development
- **Faker** – Python library for generating fake data
- **Git & GitHub** – Version control and repository hosting
- **Virtualenv** – Virtual environment for dependency management

---

## ⚙️ Installation & Setup  

### Prerequisites  
- Python 3.x installed  
- Git installed  
- `virtualenv` installed  

### Steps  

1.  **Clone the repository**  
    ```bash
    git clone https://github.com/oaappp/PSUSphere.git
    ```

2.  **Create and activate a virtual environment**  

    ```bash
    virtualenv psuenv
    ```

    **▶ Windows**  
    ```bash
    psuenv\Scripts\activate
    ```  

    **▶ macOS / Linux**  
    ```bash
    source psuenv/bin/activate
    ```  

3.  **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navigate to the project directory**  
    ```bash
    cd PSUSphere/projectsite
    ```

5.  **Apply database migrations**  
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser account**  
    ```bash
    python manage.py createsuperuser
    ```
    *(Follow the prompts to set username, email, and password)*  

7.  **Generate initial fake data**  
    ```bash
    python manage.py create_initial_data
    ```

8.  **Run the development server**  
    ```bash
    python manage.py runserver
    ```

9.  **Access the Admin Panel**  
    Open your browser and go to:  
    ```
    http://127.0.0.1:8000/admin/
    ```  
    Log in with the superuser credentials you created in **Step 6**.  

---

## 👥 Authors  

- **John Paolo Narvasa**  
- **Jude Michael Gigante**  

💡 *Developed as part of the Application Development course at Palawan State University.*  