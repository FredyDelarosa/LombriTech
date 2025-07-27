from fastapi import Depends
from sqlalchemy.orm import Session
from reports.core.Database import get_db
from reports.infrastructure.adapters.report_repository_mysql import ReportRepository
from reports.application.get_reporte_general_usecase import GetReporteGeneralUseCase
from reports.infrastructure.handlers.report_handler import ReportController

def get_report_repository(db: Session = Depends(get_db)) -> ReportRepository:
    return ReportRepository(db)

def get_report_usecase(
    repo: ReportRepository = Depends(get_report_repository)
) -> GetReporteGeneralUseCase:
    return GetReporteGeneralUseCase(repo)

def get_report_controller(
    use_case: GetReporteGeneralUseCase = Depends(get_report_usecase)
) -> ReportController:
    return ReportController(use_case)
