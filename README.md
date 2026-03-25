# MediCare Clinic Management System

A simple full-stack medical management project built with FastAPI for the backend and HTML, CSS, and JavaScript for the frontend.

This project allows users to:
- View clinic API status
- View doctors
- Add new doctors
- View appointments
- Create appointments

The application uses in-memory storage, so data resets whenever the backend server restarts.

## Project Overview

This project is designed as a lightweight clinic management demo. It includes:
- A FastAPI backend that provides REST API endpoints
- A static frontend UI built with vanilla HTML, CSS, and JavaScript
- Basic support for doctor and appointment management
- CORS support so the frontend can communicate with the backend

## Features

### Backend
- FastAPI-based REST API
- In-memory doctor and appointment storage
- API endpoints for doctors and appointments
- Duplicate doctor validation
- Doctor availability check before creating appointments
- Automatic appointment ID generation

### Frontend
- Clean clinic dashboard UI
- API status indicator
- View doctors list
- Add doctor form
- View appointments list
- Create appointment form
- Error handling for failed API requests

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

### Frontend
- HTML
- CSS
- JavaScript

## Project Structure

```text
IN226011502_FastAPI_Final_Project/
|
|-- backend/
|   |-- app/
|   |   `-- main.py
|   `-- requirements.txt
|
|-- frontend/
|   |-- index.html
|   `-- style.css
|
|-- Output/
|-- venv/
|-- .gitignore
`-- README.md
```

## API Endpoints

### Base

#### `GET /`
Returns a welcome message.

Response:

```json
{
  "message": "Welcome to MediCare Clinic"
}
```

### Doctors

#### `GET /doctors`
Returns all doctors and available doctor count.

Response:

```json
{
  "total": 3,
  "available_count": 2,
  "data": []
}
```

#### `POST /doctors`
Adds a new doctor.

Request body:

```json
{
  "name": "Dr. Smith",
  "specialization": "Cardiology",
  "fee": 300,
  "experience_years": 10,
  "is_available": true
}
```

### Appointments

#### `GET /appointments`
Returns all appointments.

Response:

```json
{
  "total": 1,
  "data": []
}
```

#### `POST /appointments`
Creates a new appointment.

Request body:

```json
{
  "patient_name": "John Doe",
  "doctor_id": 1,
  "date": "2026-03-25",
  "appointment_type": "consultation"
}
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd IN226011502_FastAPI_Final_Project
```

### 2. Create and Activate Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

### 3. Install Dependencies

```powershell
pip install -r .\backend\requirements.txt
```

### 4. Run the Backend

```powershell
cd .\backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Backend will run at:

```text
http://127.0.0.1:8000/
```

### 5. Run the Frontend

Open a new terminal from the project root and run:

```powershell
.\venv\Scripts\Activate.ps1
cd .\frontend
python -m http.server 8080
```

Frontend will run at:

```text
http://127.0.0.1:8080/
```

## How the Frontend Works

The frontend is a static website, so it does not require React, Angular, or Node.js.

It communicates with the backend using JavaScript `fetch()` requests.

The UI:
- Detects backend availability
- Displays API status
- Fetches doctors and appointments
- Sends JSON data to backend endpoints

## Important Notes

- This project uses in-memory storage
- Data is not saved permanently
- Restarting the FastAPI server resets doctors and appointments
- The frontend must be served from the `frontend` folder using `python -m http.server`

## Sample Workflow

1. Start backend server
2. Start frontend server
3. Open the frontend in browser
4. Click `Get Doctors` to view doctors
5. Add a new doctor using the form
6. Create an appointment using an available doctor
7. Refresh appointments to verify the new record

## Common Issues and Fixes

### Frontend not opening

Make sure you are running:

```powershell
cd .\frontend
python -m http.server 8080
```

Then open:

```text
http://127.0.0.1:8080/
```

Do not open `index.html` directly by double-clicking.

### Backend works but frontend cannot connect

Make sure backend is running on:

```text
http://127.0.0.1:8000/
```

### Port already in use

Use another port for frontend:

```powershell
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500/
```

### Git push rejected

If the GitHub repo already has files like `README.md`, pull first:

```powershell
git pull origin main --allow-unrelated-histories
```

Resolve conflicts if needed, then:

```powershell
git add .
git commit -m "Resolve merge conflict"
git push -u origin main
```

## Future Improvements

- Database integration using SQLite or MySQL
- User authentication
- Update and delete APIs
- Better appointment scheduling rules
- Persistent storage
- Search and filter features
- Improved UI design and responsiveness

## Author

Parshwa Desai

## License

This project is for educational and learning purposes.
