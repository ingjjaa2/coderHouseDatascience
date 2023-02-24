from pydantic import BaseModel

class Input_Validation(BaseModel):
    Prof: float
    XCOORD: float
    YCOORD: float
    Dpiston: float