from fastapi import APIRouter, Depends, HTTPException
from reports.infrastructure.handlers.report_handler import ReportController
from reports.infrastructure.deps import get_report_controller

router = APIRouter(prefix="/reportes", tags=["reportes"])

@router.get("/{composta_id}")
def get_reporte(composta_id: int, controller: ReportController = Depends(get_report_controller)):
    result = controller.get_reporte(composta_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return result
