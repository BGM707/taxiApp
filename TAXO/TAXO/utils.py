import sqlite3

def calcular_tarifa(kilometraje, tiempo, ida_vuelta):
    conn = sqlite3.connect("taxi_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT tarifa_km, tarifa_hora, tarifa_manejo, extra_ida_vuelta FROM tarifas WHERE id = 1")
    tarifas = cursor.fetchone()
    conn.close()

    tarifa_km, tarifa_hora, tarifa_manejo, extra_ida_vuelta = tarifas
    costo_total = (
        (kilometraje * tarifa_km) +
        (tiempo * tarifa_hora) +
        tarifa_manejo +
        (extra_ida_vuelta if ida_vuelta else 0)
    )
    return costo_total