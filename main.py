from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Admin password stored in backend (Not visible to frontend)
ADMIN_PASSWORD = "9775462183"

# Allow all origins (so your website can call it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordCheck(BaseModel):
    password: str

@app.post("/auth")
def check_password(data: PasswordCheck):
    if data.password == ADMIN_PASSWORD:
        return { "ok": True }
    else:
        return { "ok": False }