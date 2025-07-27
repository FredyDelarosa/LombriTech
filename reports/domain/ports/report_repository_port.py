from typing import Protocol, Optional

class IReportRepository(Protocol):
    def get_reporte_general(self, composta_id: int) -> Optional[dict]:
        ...
