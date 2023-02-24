from pydantic import BaseModel

class Validador(BaseModel):
    Prof: float
    XCOORD: float
    YCOORD: float
    Dpiston: float