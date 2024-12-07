from dataclasses import dataclass
from typing import Optional
from .location_scraper import FuelStation

@dataclass
class FuelCost:
    costo_combustible: float
    precio_por_litro: float
    litros_necesarios: float
    estacion_servicio: Optional[FuelStation] = None

class FuelCalculator:
    @staticmethod
    def calcular_costo_combustible(
        distancia: float,
        rendimiento: float,
        estacion: FuelStation,
        tipo_combustible: str
    ) -> Optional[FuelCost]:
        """
        Calcula el costo del combustible para un viaje.
        
        Args:
            distancia: Distancia en kilómetros
            rendimiento: Rendimiento del vehículo en km/l
            estacion: Estación de servicio seleccionada
            tipo_combustible: Tipo de combustible ('93', '95', '97', 'diesel')
        
        Returns:
            FuelCost object con los detalles del cálculo
        """
        try:
            # Obtiene el precio según el tipo de combustible
            precio = None
            if tipo_combustible == '93':
                precio = estacion.precio_93
            elif tipo_combustible == '95':
                precio = estacion.precio_95
            elif tipo_combustible == '97':
                precio = estacion.precio_97
            elif tipo_combustible == 'diesel':
                precio = estacion.precio_diesel
            
            if precio is None:
                return None
            
            # Calcula los litros necesarios
            litros = distancia / rendimiento
            
            # Calcula el costo total
            costo = litros * precio
            
            return FuelCost(
                costo_combustible=costo,
                precio_por_litro=precio,
                litros_necesarios=litros,
                estacion_servicio=estacion
            )
        except Exception as e:
            print(f"Error al calcular costo de combustible: {e}")
            return None