from typing import Optional
from sqlalchemy.orm import Session
from reports.domain.entities.composta import Composta
from reports.domain.entities.lote import Lote
from reports.domain.entities.usuarios import Usuario
from reports.domain.entities.temperatura import Temperatura
from reports.domain.entities.humedad import Humedad
from reports.domain.entities.ph import Ph
from reports.domain.ports.report_repository_port import IReportRepository

class ReportRepository(IReportRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_reporte_general(self, composta_id: int) -> Optional[dict]:
        composta_row = self.db.execute(
            "SELECT * FROM composta WHERE id = :id", {"id": composta_id}
        ).fetchone()
        if not composta_row:
            return None

        lote_row = self.db.execute(
            "SELECT * FROM lote WHERE id = :id", {"id": composta_row.lote_id}
        ).fetchone()

        usuario_row = self.db.execute(
            "SELECT * FROM usuarios WHERE id = :id", {"id": composta_row.usuario_id}
        ).fetchone()

        temp_row = self.db.execute(
            "SELECT * FROM temperatura WHERE composta_id = :cid ORDER BY fecha ASC LIMIT 1", {"cid": composta_id}
        ).fetchone()

        humedad_row = self.db.execute(
            "SELECT * FROM humedad WHERE composta_id = :cid ORDER BY fecha ASC LIMIT 1", {"cid": composta_id}
        ).fetchone()

        ph_row = self.db.execute(
            "SELECT * FROM ph WHERE composta_id = :cid ORDER BY fecha ASC LIMIT 1", {"cid": composta_id}
        ).fetchone()

        return {
            "usuario": {
                "nombre_completo": f"{usuario_row.nombre} {usuario_row.apellidos}" if usuario_row else None,
                "correo": usuario_row.correo if usuario_row else None,
                "rol": usuario_row.rol if usuario_row else None,
            },
            "proceso": {
                "fecha_inicio": lote_row.fecha_inicio if lote_row else None,
                "fecha_final": lote_row.fecha_final if lote_row else None,
                "tipo_sustrato": lote_row.descripcion if lote_row else None,
                "lombrices_inicial": composta_row.cant_lom_inicial,
                "lombrices_final": composta_row.cant_lom_final,
            },
            "sensores_iniciales": {
                "temperatura": temp_row.dato if temp_row else None,
                "humedad": humedad_row.dato if humedad_row else None,
                "ph": ph_row.dato if ph_row else None,
            }
        }
