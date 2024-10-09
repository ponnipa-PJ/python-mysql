from datetime import datetime
import re

def validateBirthdate(birthDate_str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"  # รูปแบบ YYYY-MM-DD
    
    if not re.match(pattern, birthDate_str):
        return False, "Invalid birth date format, should be YYYY-MM-DD"
    
    # ตรวจสอบความถูกต้องของวัน
    try:
        birth_date = datetime.strptime(birthDate_str, "%Y-%m-%d").date()
        return True, birth_date
    except ValueError:
        return False, "Invalid birth date"
