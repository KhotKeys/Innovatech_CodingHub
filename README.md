# Innovatech CodingHub

# Students Learning Platform


# Link to the slide
[Click here](https://docs.google.com/presentation/d/1qKl3PCPYqUwRW8_hhTn0iTUWvbM_xlDXx2QDAt8A0as/edit#slide=id.g2e6a755ee06_1_26)

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
  - [Recycling Test](#recycling-test)
  - [User Authentication Test](#user-authentication-test)
- [CI/CD Pipeline](#cicd-pipeline)
- [License](#license)
- [Contributor](#contributor)

## Overview

Innovatech CodingHub the Students Learning Platform is an innovative web application designed to streamline learning processes for the students and other learners, and administrators. The system aims to enhance waste collection learning efficiency, promote education technology efforts, and provide insights into education technology impact metrics.

## Features

- **User Registration and Login**: Secure user authentication and session management.
- **Courses Accessibility**: Courses on the platform.
- **Admin Dashboard**: Monitor system performance, manage users, and generate reports.

## Prerequisites

Ensure you have the following before starting:
- Jango (version 12.x or higher)
- PostgreSQL or MySQL

## Installation

Clone the repository:

```bash
git clone https://github.com/KhotKeys/Innovatech_CodingHub.git
cd Innovatech_CodingHub
```

Install the dependencies:

```bash
npm install
```

Set up the database by running migrations:

```bash
npx sequelize-cli db:migrate
```

## Repository Structure

When you clone the repository, you'll find the following directories and files:
- **`frontend/`**: Contains the HTML, CSS, and JavaScript files for the frontend.
- **`backend/`**: Contains the backend code including routes, models, and middleware.
- **`admin/`**: Contains the HTML, CSS, and JavaScript files for the admin interface.
- **`models/`**: Defines the database models.
- **`routes/`**: Contains the route handlers for different functionalities.
- **`middleware/`**: Contains middleware for authentication and error handling.
- **`config/`**: Configuration files for the database and environment settings.

## Usage

### Running the Application

To run the application, navigate to the project directory in your terminal and start the server:

```bash
npm dev
```

This command will start the server and the application will be accessible at `(https://innovatech.pythonanywhere.com/login)`.

```

*Importance Credentials*

Certificate: 	2b91cdcdd55f62c7b89dca63475555cbb90820e29475ac2434b766a9ef4ddb13
Public Key:	17d2f71848e5c9a1657cd956cf28b019d440eee726e0a66c54731e799388ac5f

```

### Waste Collection Schedule

- **Register and login**: Users can access resources turtorials and learn sort of programming and coding Languages.
  ```bash
  POST /api/schedules
  {
    "date": "YYYY-MM-DD",
    "time": "HH:MM"
  }
  ```
- **Get Courses**: Retrieve all courses collections for a user.
  ```bash
  GET /api/courses
  ```

### User Management

- **Get All Users**: Retrieve all users for the admin.
  ```bash
  GET /api/admin/users
  ```

## Testing

### register Test

To test the registration functionality, use tools like Postman or CURL to send requests to the `/api/register` endpoint.

### login Test

To test the login functionality, use tools like Postman or CURL to send requests to the `/api/login` endpoint.

### User Authentication Test

#### Example `tests/auth.test.js`

```python
const request = require('supertest');
const app = require('../app'); // make sure the path is correct

describe('User Authentication', () => {
  it('should signup a new user', async () => {
    const res = await request(app)
      .post('/api/auth/signup')
      .send({
        firstname: 'gabriel',
        lastname: 'Pawuoi',
        email: 'gabriel@example.com',
        password: 'secret123',
        address: '123 Main St'
      });
    expect(res.statusCode).toBe(201);
    expect(res.body.message).toContain('registered successfully');
  });

  it('should login an existing user', async () => {
    const res = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'gabriel@example.com',
        password: 'secret123'
      });
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('token');
  });

  it('should not login with incorrect credentials', async () => {
    const res = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'gabriel@example.com',
        password: 'wrongpassword'
      });
    expect(res.statusCode).toBe(400);
    expect(res.body.error).toContain('Invalid credentials');
  });
});
```

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions. You can find the configuration in the `.github/workflows/ci-cd.yml` file.

## Contributing

Contributions are welcome. Please fork the repository, create a feature branch, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Project owner
- **Gabriel** - [GitHub Profile](https://github.com/KhotKeys)

## Live Applications

- **Web Application:** [https://innovatech.pythonanywhere.com](https://innovatech.pythonanywhere.com/login)
- **Admin Web Application:** [https://innovatech.pythonanywhere.com](https://innovatech.pythonanywhere.com/login)
  - **Admin Credentials:**
    - **Email:** admin@admin.com
    - **Password:** admin

## Happy Ending 🎉
