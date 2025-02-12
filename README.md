# DjangoResume 🎓💼

A **Django-based resume builder** web application that allows users to create and manage their professional resumes easily.

## 🚀 Features
- 🔐 **User Authentication** (Login/Signup)
- 📝 **Resume Creation** with multiple sections
- 📄 **Download Resume as PDF**
- ⚙️ **Admin Panel** for managing resumes
- 🎨 **Responsive UI** for seamless experience

---

## 🛠️ Installation Guide

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/prasadsheetal/DjangoResume.git
cd DjangoResume
2️⃣ Create a Virtual Environment (Recommended)
sh
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install Django manually:

sh
Copy
Edit
pip install django
4️⃣ Apply Migrations
sh
Copy
Edit
python manage.py migrate
5️⃣ Create a Superuser (Optional)
sh
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up an admin user.

6️⃣ Run the Development Server
sh
Copy
Edit
python manage.py runserver
The app will be available at http://127.0.0.1:8000/.

📂 Project Structure
csharp
Copy
Edit
DjangoResume/
│── resume/              # Main Django app
│── templates/           # HTML templates
│── static/              # Static files (CSS, JS, Images)
│── manage.py            # Django management script
│── db.sqlite3           # Database file (if using SQLite)
│── requirements.txt     # Dependencies list
│── README.md            # Project documentation
🔧 Troubleshooting
❌ "ModuleNotFoundError: No module named 'django'"
Run:

sh
Copy
Edit
pip install django
❌ "manage.py not found"
Make sure you are inside the correct directory:

sh
Copy
Edit
cd DjangoResume
❌ Database Issues
Try:

sh
Copy
Edit
python manage.py makemigrations
python manage.py migrate
📸 Screenshots
Add screenshots of the UI here.

🌐 Deployment (Optional)
To deploy this Django project using Heroku, follow these steps:

Install Heroku CLI:
sh
Copy
Edit
curl https://cli-assets.heroku.com/install.sh | sh
Login to Heroku:
sh
Copy
Edit
heroku login
Create a Heroku App:
sh
Copy
Edit
heroku create your-app-name
Add gunicorn to requirements.txt and create a Procfile:
sh
Copy
Edit
echo "web: gunicorn DjangoResume.wsgi --log-file -" > Procfile
Push to Heroku:
sh
Copy
Edit
git add .
git commit -m "Deploy to Heroku"
git push heroku main
Run migrations on Heroku:
sh
Copy
Edit
heroku run python manage.py migrate
Open the app:
sh
Copy
Edit
heroku open
🤝 Contributing
Contributions are welcome!
To contribute:

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m "Add new feature")
Push to your fork (git push origin feature-branch)
Open a Pull Request
📜 License
This project is licensed under the MIT License.

🎯 Author
Sheetal Prasad
GitHub: @prasadsheetal
LinkedIn: Profile
