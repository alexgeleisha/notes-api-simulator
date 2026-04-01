# api/utils.py
from datetime import datetime
def now():
    return datetime.now().isoformat()
