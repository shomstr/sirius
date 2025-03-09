from pydantic import BaseModel
from typing import List, Optional

class ConnectorBase(BaseModel):
    id: str
    name: Optional[str]
    active: bool
    connector: str
    power: int
    state: str
    changed_at: str

class EVSEBase(BaseModel):
    id: str
    state: str
    changed_at: str
    connectors: List[ConnectorBase]

class StationBase(BaseModel):
    id: int
    active: bool
    name: str
    description: Optional[str]
    coordinates: List[float]
    address: str
    city: Optional[str]
    time_zone: str
    changed_at: str
    evses: List[EVSEBase]

class StationCreate(StationBase):
    pass

class StationUpdate(StationBase):
    pass