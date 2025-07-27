from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioReporte(BaseModel):
    nombre_completo: Optional[str]
    correo: Optional[str]
    rol: Optional[str]

class ProcesoReporte(BaseModel):
    fecha_inicio: Optional[date]
    fecha_final: Optional[date]
    tipo_sustrato: Optional[str]
    lombrices_inicial: Optional[int]
    lombrices_final: Optional[int]

class SensoresInicialesReporte(BaseModel):
    temperatura: Optional[float]
    humedad: Optional[float]
    ph: Optional[float]

class ReporteGeneral(BaseModel):
    usuario: UsuarioReporte
    proceso: ProcesoReporte
    sensores_iniciales: SensoresInicialesReporte
