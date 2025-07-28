def obtener_valores_individuales_reales():
	from sqlalchemy import text
	from core.db.Database import SessionLocal
	db = SessionLocal()
	try:
		query = text("""
		SELECT
		(SELECT dato FROM Ph ORDER BY fecha DESC LIMIT 1) AS ph,
		(SELECT dato FROM Humedad ORDER BY fecha DESC LIMIT 1) AS humedad,
		(SELECT dato FROM Temperatura ORDER BY fecha DESC LIMIT 1) AS temperatura,
		(SELECT ec FROM C_electrica ORDER BY fecha DESC LIMIT 1) AS ec,
		(SELECT tds FROM C_electrica ORDER BY fecha DESC LIMIT 1) AS tds,
		(SELECT sst FROM Turbidez ORDER BY fecha DESC LIMIT 1) AS sst
		""")
		result = db.execute(query).fetchone()
		return dict(result._mapping)
	finally:
		db.close()