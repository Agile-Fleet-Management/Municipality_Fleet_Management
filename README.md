# Municipality Fleet Management

## Introduction
The Municipality Fleet Management system is a web application designed to help manage the fleet of vehicles owned by the municipality. With this system, users can keep track of vehicle maintenance schedules, usage logs, and other logistical details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- PostgreSQL
- Git

### Installation

1. **Clone the repository**
    ```bash
    git clone https://your-repository-url-here.git
    cd Municipality_Fleet_Management
    ```

2. **Set up a Python virtual environment and activate it**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS and Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```
4. **Example of creating an app**
    ```bash
    python manage.py startapp users apps/users
    ```
### Database Setup

1. **Ensure PostgreSQL is installed and running on your local machine. Then, create a database with the following credentials:**

```plaintext
Database Name: fleet_management
Database User: postgres
Database Password: password
Host: localhost
Port: 5432

3. **Run migrations**

    ```bash
    python manage.py migrate
    ```

### Running the Development Server

Start the development server with:

```bash
python manage.py runserver
## Creating a Personal Branch
Before you start working on a new feature or a fix, create a new branch with your name from the main branch:
```
```bash
git checkout -b feature/<your-name>
# or
git checkout -b fix/<your-name>
```
