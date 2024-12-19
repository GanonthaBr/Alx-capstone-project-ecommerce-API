# My Cosmetic Natural Project

## Setup Instructions

Follow these steps to set up the Django project on your local machine.

### Prerequisites

- Python 3.x
- pip
- virtualenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GanonthaBr/alx-Backend-Django-capstone-project.git
   cd mycosmeticnaturalproject
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply the migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the project:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

### Additional Notes

- To deactivate the virtual environment, simply run:

  ```bash
  deactivate
  ```

- Make sure to configure your database settings in `settings.py` if you are using a database other than SQLite.

- For any additional configuration, refer to the Django documentation.
