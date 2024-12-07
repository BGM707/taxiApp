import requests
from typing import Dict, Optional

class CombustibleAPI:
    @staticmethod
    def obtener_precio_combustible(region: str, tipo_combustible: str) -> Optional[float]:
        try:
            # Esta es una URL de ejemplo - deberás reemplazarla con la API real
            url = f"https://api.ejemplo.cl/combustibles/{region}/{tipo_combustible}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data.get("precio")
            return None
        except Exception as e:
            print(f"Error al obtener precio de combustible: {e}")
            return None

    @staticmethod
    def calcular_costo_combustible(distancia: float, rendimiento: float, precio_combustible: float) -> float:
        return (distancia / rendimiento) * precio_combustible