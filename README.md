# Municipality Fleet Management

## Introduction
Welcome to the Municipality Fleet Management system! This project is designed to streamline the management of municipal vehicles, making it easier to track maintenance, usage, and logistical information. Our aim is to provide a robust solution to manage the fleet effectively and efficiently.

## Getting Started

To get the project running locally on your machine, follow the steps outlined below.

### Prerequisites

You'll need to have the following installed to run the project:

- Python 3.8+
- pip (Python package manager)
- Virtualenv (tool to create isolated Python environments)
- PostgreSQL

### Setting Up a Development Environment

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yibork/Municipality_Fleet_Management.git
    cd Municipality_Fleet_Management
    ```

2. Create a virtual environment and activate it:

    **For macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **For Windows:**
    ```cmd
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Setting Up the Database

Ensure PostgreSQL is installed and running on your local machine. Then, create a database with the following credentials:

```plaintext
Database Name: fleet_management
Database User: postgres
Database Password: password
Host: localhost
Port: 5432
