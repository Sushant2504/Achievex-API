from pydantic import BaseModel
from typing import Optional

class ChapterwiseBase(BaseModel):
    exam: str
    subject: str
    set_no: int
    chapter_name: str
    question_no: int
    question: str
    year: int
    image: str
    option_A: str
    option_B: str
    option_C: str
    option_D: str
    answer: str
    explanation: Optional[str]
    
    
class FullTestAPI(BaseModel):
    exam: str
    subject: str
    set_no: int
    question_no: int
    question: str
    year: int
    option_A: str
    option_B: str
    option_C: str
    option_D: str
    answer: str
    explanation: Optional[str]
