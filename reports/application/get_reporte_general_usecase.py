from typing import Optional
from reports.domain.ports.report_repository_port import IReportRepository

class GetReporteGeneralUseCase:
    def __init__(self, report_repo: IReportRepository):
        self.report_repo = report_repo

    def execute(self, composta_id: int) -> Optional[dict]:
        return self.report_repo.get_reporte_general(composta_id)
