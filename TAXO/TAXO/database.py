import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect("taxi_app.db")
    cursor = conn.cursor()
    
    # Viajes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS viajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            rut TEXT,
            fecha TEXT,
            direccion_partida TEXT,
            direccion_destino TEXT,
            kilometraje REAL,
            tiempo REAL,
            ida_vuelta BOOLEAN,
            costo_total REAL,
            conductor_id INTEGER,
            vehiculo_id INTEGER,
            FOREIGN KEY (conductor_id) REFERENCES conductores (id),
            FOREIGN KEY (vehiculo_id) REFERENCES vehiculos (id)
        )
    """)
    
    # Conductores table with photo
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conductores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            rut TEXT UNIQUE,
            telefono TEXT,
            email TEXT,
            licencia_categoria TEXT,
            licencia_vencimiento TEXT,
            foto BLOB
        )
    """)
    
    # Vehículos table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            modelo TEXT,
            ano INTEGER,
            tipo_combustible TEXT,
            rendimiento REAL,
            patente TEXT UNIQUE,
            conductor_id INTEGER,
            FOREIGN KEY (conductor_id) REFERENCES conductores (id)
        )
    """)
    
    # Tarifas table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarifas (
            id INTEGER PRIMARY KEY,
            tarifa_km REAL DEFAULT 0,
            tarifa_hora REAL DEFAULT 0,
            tarifa_manejo REAL DEFAULT 0,
            extra_ida_vuelta REAL DEFAULT 0
        )
    """)
    
    # Settings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            theme_mode TEXT DEFAULT 'light'
        )
    """)
    
    # Insert default values
    cursor.execute("INSERT OR IGNORE INTO tarifas (id) VALUES (1)")
    cursor.execute("INSERT OR IGNORE INTO settings (id) VALUES (1)")
    
    conn.commit()
    conn.close()