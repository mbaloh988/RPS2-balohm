from dataclasses import dataclass

@dataclass(slots=True)
class DnevnikObj:
    ID: int = 0
    DatumCas: str = ""
    Visina: float = 0.0
    Teza: float = 0.0
    Itm: float = 0.0