from datetime import datetime

class Ticket:
    def __init__(self,message, category=None, created_at=None):
        self.message = message
        self.category = category
        self.created_at = created_at or datetime.now()
