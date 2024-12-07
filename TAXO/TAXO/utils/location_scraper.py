import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Location:
    region: str
    comuna: str
    ciudad: str

@dataclass
class FuelStation:
    nombre: str
    direccion: str
    region: str
    comuna: str
    precio_93: Optional[float]
    precio_95: Optional[float]
    precio_97: Optional[float]
    precio_diesel: Optional[float]
    ultima_actualizacion: str

class LocationScraper:
    @staticmethod
    def obtener_regiones() -> List[str]:
        """Obtiene la lista de regiones disponibles."""
        url = "https://www.bencinaenlinea.cl/web2/buscador.php"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Busca el selector de regiones
            select_region = soup.find('select', {'name': 'reg_id'})
            if not select_region:
                return []
            
            # Extrae las regiones
            regiones = []
            for option in select_region.find_all('option'):
                if option.get('value') and option.text.strip():
                    regiones.append(option.text.strip())
            
            return regiones
        except Exception as e:
            print(f"Error al obtener regiones: {e}")
            return []

    @staticmethod
    def obtener_comunas(region: str) -> List[str]:
        """Obtiene la lista de comunas para una región específica."""
        url = "https://www.bencinaenlinea.cl/web2/buscador.php"
        try:
            # Aquí deberías hacer una petición POST con la región seleccionada
            # para obtener las comunas correspondientes
            data = {'reg_id': region}
            response = requests.post(url, data=data)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Busca el selector de comunas
            select_comuna = soup.find('select', {'name': 'com_id'})
            if not select_comuna:
                return []
            
            # Extrae las comunas
            comunas = []
            for option in select_comuna.find_all('option'):
                if option.get('value') and option.text.strip():
                    comunas.append(option.text.strip())
            
            return comunas
        except Exception as e:
            print(f"Error al obtener comunas: {e}")
            return []

    @staticmethod
    def obtener_estaciones(region: str, comuna: str) -> List[FuelStation]:
        """Obtiene las estaciones de servicio y sus precios para una ubicación específica."""
        url = "https://www.bencinaenlinea.cl/web2/buscador.php"
        try:
            # Realiza la búsqueda de estaciones
            data = {
                'reg_id': region,
                'com_id': comuna,
                'buscar': 'Buscar'
            }
            response = requests.post(url, data=data)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Busca la tabla de resultados
            tabla = soup.find('table', {'class': 'tabla_precios'})
            if not tabla:
                return []
            
            # Extrae la información de las estaciones
            estaciones = []
            for fila in tabla.find_all('tr')[1:]:  # Ignora la fila de encabezados
                cols = fila.find_all('td')
                if len(cols) >= 8:
                    estacion = FuelStation(
                        nombre=cols[0].text.strip(),
                        direccion=cols[1].text.strip(),
                        region=region,
                        comuna=comuna,
                        precio_93=float(cols[3].text.strip().replace('$', '').replace('.', '')) if cols[3].text.strip() else None,
                        precio_95=float(cols[4].text.strip().replace('$', '').replace('.', '')) if cols[4].text.strip() else None,
                        precio_97=float(cols[5].text.strip().replace('$', '').replace('.', '')) if cols[5].text.strip() else None,
                        precio_diesel=float(cols[6].text.strip().replace('$', '').replace('.', '')) if cols[6].text.strip() else None,
                        ultima_actualizacion=cols[7].text.strip()
                    )
                    estaciones.append(estacion)
            
            return estaciones
        except Exception as e:
            print(f"Error al obtener estaciones: {e}")
            return []