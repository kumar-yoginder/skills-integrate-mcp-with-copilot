"""
User management for authentication and roles
"""
from typing import Optional, Dict
from fastapi import HTTPException
import hashlib

# In-memory user database
users = {
    # Example teacher/admin
    "teacher1@mergington.edu": {
        "password": hashlib.sha256(b"adminpass").hexdigest(),
        "role": "admin"
    },
    # Example student
    "student1@mergington.edu": {
        "password": hashlib.sha256(b"studentpass").hexdigest(),
        "role": "student"
    }
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(email: str, password: str) -> Dict:
    user = users.get(email)
    if not user or user["password"] != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"email": email, "role": user["role"]}

def register(email: str, password: str, role: str = "student") -> Dict:
    if email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[email] = {"password": hash_password(password), "role": role}
    return {"email": email, "role": role}

def get_user_role(email: str) -> Optional[str]:
    user = users.get(email)
    return user["role"] if user else None
