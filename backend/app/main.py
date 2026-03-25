#IMPORTS
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data
doctors = [
    {"id": 1, "name": "Dr. Alice", "specialization": "Cardiology", "fee": 200, "experience_years": 10, "is_available": True},
    {"id": 2, "name": "Dr. Bob", "specialization": "Dermatology", "fee": 150, "experience_years": 8, "is_available": True},
    {"id": 3, "name": "Dr. Charlie", "specialization": "Neurology", "fee": 250, "experience_years": 12, "is_available": False}
]

appointments = [
    {"appointment_id": 1, "patient": "John Doe", "doctor_id": 1, "date": "2023-10-01", "type": "consultation", "original_fee": 200, "final_fee": 200, "status": "scheduled"}
]


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    fee: int = Field(ge=0)
    experience_years: int = Field(ge=0)
    is_available: bool = True


class AppointmentCreate(BaseModel):
    patient_name: str
    doctor_id: int = Field(ge=1)
    date: str
    appointment_type: str

#BASIC
@app.get("/")
def home():
    return {"message": "Welcome to MediCare Clinic"}

#DOCTORS
@app.get("/doctors")
def get_doctors():
    available = [d for d in doctors if d["is_available"]]
    return {
        "total": len(doctors),
        "available_count": len(available),
        "data": doctors
    }

@app.post("/doctors")
def add_doctor(payload: DoctorCreate):
    if any(d["name"].lower() == payload.name.lower() for d in doctors):
        raise HTTPException(400, "Duplicate doctor")
    new_id = max(d["id"] for d in doctors) + 1 if doctors else 1
    doctor = {
        "id": new_id,
        "name": payload.name,
        "specialization": payload.specialization,
        "fee": payload.fee,
        "experience_years": payload.experience_years,
        "is_available": payload.is_available
    }
    doctors.append(doctor)
    return {"message": "Doctor added", "doctor": doctor}

#APPOINTMENTS
@app.get("/appointments")
def get_appts():
    return {"total": len(appointments), "data": appointments}

@app.post("/appointments")
def create_appt(payload: AppointmentCreate):
    doctor = next((d for d in doctors if d["id"] == payload.doctor_id), None)
    if not doctor:
        raise HTTPException(404, "Doctor not found")
    if not doctor["is_available"]:
        raise HTTPException(400, "Doctor not available")
    new_id = max(a["appointment_id"] for a in appointments) + 1 if appointments else 1
    appt = {
        "appointment_id": new_id,
        "patient": payload.patient_name,
        "doctor_id": payload.doctor_id,
        "date": payload.date,
        "type": payload.appointment_type,
        "original_fee": doctor["fee"],
        "final_fee": doctor["fee"],
        "status": "scheduled"
    }
    appointments.append(appt)
    doctor["is_available"] = False
    return {"message": "Appointment created", "appointment": appt}
