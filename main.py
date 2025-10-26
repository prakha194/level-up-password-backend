import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import bcrypt

app = FastAPI()

# Allow your frontend to call the backend (you can restrict domain later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read password from Render Environment Variable
ADMIN_PASS = os.getenv("ADMIN_PASS")
if not ADMIN_PASS:
    raise Exception("ADMIN_PASS environment variable is not set on Render.")

# Hash password once on startup
HASHED_PASSWORD = bcrypt.hashpw(ADMIN_PASS.encode("utf-8"), bcrypt.gensalt())

class PasswordPayload(BaseModel):
    password: str

@app.post("/auth")
def auth(payload: PasswordPayload):
    if bcrypt.checkpw(payload.password.encode("utf-8"), HASHED_PASSWORD):
        return {"ok": True}
    return {"ok": False}
