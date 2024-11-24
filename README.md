# Innovatech CodingHub

## Student Learning Platform

### Link to the Slide  
[Click here](https://docs.google.com/presentation/d/1qKl3PCPYqUwRW8_hhTn0iTUWvbM_xlDXx2QDAt8A0as/edit#slide=id.g2e6a755ee06_1_26)

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [User Management](#user-management)
- [Testing](#testing)
  - [Registration Test](#registration-test)
  - [Login Test](#login-test)
- [CI/CD Pipeline](#cicd-pipeline)
- [License](#license)
- [Contributing](#contributing)
- [Project Owner](#project-owner)
- [Live Application](#live-application)

---

## Overview

**Innovatech CodingHub** is an innovative web application designed to streamline the learning process for students and educators. It offers course accessibility, secure user management, and administrative tools to enhance productivity and learning outcomes. The platform leverages education technology to improve engagement and provide insights into learning impact metrics.

---

## Features

- **User Registration and Login**: Secure authentication and session management with role-based access.
- **Courses Accessibility**: Categorized courses by topic and difficulty, accessible to all registered users.
- **Admin Dashboard**: Insights into user activities, course analytics, and system performance monitoring.

---

## Prerequisites

Before starting, ensure you have the following:
- **Python** (version 3.8 or higher)
- **Django** (version 4.x or higher)
- **PostgreSQL** or **MySQL**
- **pipenv** for managing dependencies

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KhotKeys/Innovatech_CodingHub.git
    cd Innovatech_CodingHub
    ```

2. **Install dependencies**:
    ```bash
    pipenv install
    ```

3. **Set up the database**:
    ```bash
    pipenv run flask db init
    pipenv run flask db migrate
    pipenv run flask db upgrade
    ```

4. **Start the application**:
    ```bash
    pipenv run flask run
    ```

The application will be accessible at:  
[https://innovatech.pythonanywhere.com/login](https://innovatech.pythonanywhere.com/login)

---

## Repository Structure

- **`frontend/`**: HTML, CSS, and JavaScript files for the user interface.
- **`backend/`**: Backend logic, including API routes, models, and services.
- **`admin/`**: Interface and scripts for administrative functionality.
- **`models/`**: Definitions for database schema and relationships.
- **`routes/`**: Backend route handlers for various functionalities.
- **`middleware/`**: Middleware for authentication and error handling.
- **`config/`**: Configuration files for database and environment settings.

---

## Usage

### Running the Application
Start the development server with:
```bash
pipenv run flask run
```
The application will be available at:  
[https://innovatech.pythonanywhere.com/login](https://innovatech.pythonanywhere.com/login)

### User Management
- **Get All Users** (Admin only):  
  Retrieve all registered users:
  ```bash
  GET /api/admin/users
  ```

---

## Testing

### Registration Test
Use `pytest` to test the registration functionality:
```python
def test_registration(client):
    response = client.post('/api/register', json={
        "firstname": "Gabriel",
        "lastname": "Pawuoi",
        "email": "gabriel.pawuoi@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert "registered successfully" in response.json['message']
```

### Login Test
To test the login functionality:
```python
def test_login(client):
    response = client.post('/api/login', json={
        "email": "gabriel.pawuoi@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.json
```

---

## CI/CD Pipeline

The CI/CD pipeline is set up with GitHub Actions. It includes the following steps:
- **Linting**: Ensures code adheres to style guidelines.
- **Testing**: Runs unit tests.
- **Deployment**: Deploys the application to the live server.

Configuration is in the `.github/workflows/ci-cd.yml` file.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.

---

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request for review.

---

## Project Owner

- **Gabriel**  
  GitHub: [KhotKeys](https://github.com/KhotKeys)

---

## Live Application

- **Web Application**: [https://innovatech.pythonanywhere.com/login](https://innovatech.pythonanywhere.com/login)  
- **Admin Login**:  
  - **Email**: admin@admin.com  
  - **Password**: admin

**Happy Ending🎉**
