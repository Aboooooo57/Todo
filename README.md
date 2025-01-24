
# Django Task Management API

A Django-based Task Management API for creating, retrieving, updating, and deleting tasks. It supports filtering and custom search functionality.

---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

Open your browser and navigate to:
http://localhost:{port}/swagger/
