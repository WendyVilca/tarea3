from utils.db import db
class Ubigeo(db.Model):
    __tablename__ = 'persona'
    persona_id = db.Column(db.Integer, primary_key=True)
    persona_dni = db.Column(db.String(255))

    def __init__(self, persona_id, persona_dni):
        self.persona_id = persona_id
        self.persona_dni = persona_dni