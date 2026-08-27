import re
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import database
from database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def calculate_risk_score(title: str, description: str) -> int:
    score = 0
    full_text = f"{title} {description}".lower()

    red_flags = {
        35: ["otp", "pin", "cvv", "password", "upi pin", "aadhaar", "pan card"],
        30: ["anydesk", "teamviewer", "remote access", "scan this qr code", "security deposit", "digital arrest"],
        25: ["kyc", "blocked", "suspended", "electricity bill", "deactivation", "bank account"],
        20: ["lottery", "win", "reward", "cashback", "part-time job", "telegram", "whatsapp group"]
    }

    for weight, words in red_flags.items():
        for word in words:
            if word in full_text:
                score += weight
                break 

    has_link = re.search(r'(https?://|www\.|bit\.ly|t\.me|goo\.gl)', full_text)
    has_phone = re.search(r'(\+?\d{1,3})?[-.\s]?(\d{10}|\d{5}\s\d{5})', full_text)

    if has_link: score += 25 
    if has_phone: score += 15

    urgency_words = ["urgent", "immediately", "today", "now", "expired", "permanent"]
    urgency_count = sum(1 for word in urgency_words if word in full_text)
    score += (urgency_count * 10)

  
    if has_link and ("kyc" in full_text or "verify" in full_text or "bank" in full_text):
        score += 30

    return min(score, 100)

@app.post("/report/")
def create_report(title: str, description: str, category: str, db: Session = Depends(database.get_db)):
    risk_score = calculate_risk_score(title, description)
    
    new_report = models.FraudReport(
        title=title, 
        description=description, 
        category=category, 
        risk_score=risk_score
    )
    
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    
    return {
        "status": "Analyzed", 
        "risk_score": new_report.risk_score,
        "incident_id": new_report.id
    }