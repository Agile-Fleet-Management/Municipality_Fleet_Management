# Municipality Fleet Management

## Introduction
The Municipality Fleet Management system is a web application designed to manage the fleet of vehicles owned by the municipality. This system allows users to track vehicle maintenance schedules, usage logs, and other logistical details, now with the ease of Docker containers for development, testing, and production environments.

## Getting Started
These instructions will guide you through setting up a copy of the project on your local machine for development and testing purposes using Docker.

### Prerequisites
Before you begin, ensure you have the following installed:
- Docker
- Docker Compose
- Git

Docker will manage the Python and PostgreSQL environments, so you don't need to install them separately on your local machine.

### Installation

1. **Clone the repository**
    ```bash
    git clone https://your-repository-url-here.git
    cd Municipality_Fleet_Management
    ```

2. **Build the Docker containers**

    The project includes a `Dockerfile` for the web application and a `docker-compose.yml` file that defines the services (web app and database).

    ```bash
    docker-compose build
    ```

3. **Start the Docker containers**

    ```bash
    docker-compose up
    ```

    This command starts the necessary services defined in your `docker-compose.yml`. It typically includes the web application and the PostgreSQL database service.
