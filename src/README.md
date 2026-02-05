# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities
- **User authentication and roles (student, admin/teacher)**
- **Restrict activity management to teachers/admins**

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| POST   | `/signup?email=...&password=...&role=student|admin`               | Register a new user (student or admin)                              |
| POST   | `/login?email=...&password=...`                                   | Login and create a session                                          |
| POST   | `/activities/{activity_name}/signup?email=...&password=...`       | Sign up for an activity (students only)                             |
| DELETE | `/activities/{activity_name}/unregister?email=...&password=...`   | Unregister from an activity (students only)                         |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |

## Data Model

- **Users**: email, password (hashed), role (student/admin)
- **Sessions**: in-memory, keyed by email

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
