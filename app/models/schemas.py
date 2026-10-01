from typing import List, Optional

from pydantic import BaseModel, Field


class Evidence(BaseModel):
    quote: str = Field(description="Short quote supporting the extracted information")
    source_chunk_id: str = Field(description="ID of the transcript chunk containing the evidence")


class Decision(BaseModel):
    decision: str
    status: str
    evidence: List[Evidence]
    confidence: float = Field(ge=0.0, le=1.0)


class ActionItem(BaseModel):
    task: str
    assigned_to: Optional[str] = None
    due_date: Optional[str] = None
    status: str = "open"
    evidence: List[Evidence]
    confidence: float = Field(ge=0.0, le=1.0)


class Entities(BaseModel):
    people: List[str] = []
    organizations: List[str] = []
    locations: List[str] = []
    bills: List[str] = []
    dates: List[str] = []


class MeetingOutput(BaseModel):
    summary: str
    decisions_made: List[Decision]
    action_items: List[ActionItem]
    entities: Entities