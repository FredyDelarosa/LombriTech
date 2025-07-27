from fastapi import HTTPException
from reports.application.get_reporte_general_usecase import GetReporteGeneralUseCase
from reports.infrastructure.schemas.reporte_schemas import ReporteGeneral
from sqlalchemy.orm import Session
from typing import Optional

class ReportController:
    def __init__(self, use_case: GetReporteGeneralUseCase):
        self.use_case = use_case

    def get_reporte(self, composta_id: int) -> ReporteGeneral:
        reporte_data: Optional[dict] = self.use_case.execute(composta_id)
        if not reporte_data:
            raise HTTPException(status_code=404, detail="Reporte no encontrado")

        return ReporteGeneral(**reporte_data)
