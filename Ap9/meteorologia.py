from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.temperaturas = []
        self.humedades = []
        self.presiones = []
        self.velocidades_viento = []
        self.direcciones_viento = []

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(": ")
                if len(partes) == 2:
                    clave, valor = partes
                    if clave == "Temperatura":
                        self.temperaturas.append(float(valor))
                    elif clave == "Humedad":
                        self.humedades.append(float(valor))
                    elif clave == "Presion":
                        self.presiones.append(float(valor))
                    elif clave == "Viento":
                        velocidad, direccion = valor.split(",")
                        self.velocidades_viento.append(float(velocidad))
                        self.direcciones_viento.append(direccion.strip())

        promedio_temperatura = round(sum(self.temperaturas) / len(self.temperaturas), 2)
        promedio_humedad = round(sum(self.humedades) / len(self.humedades), 2)
        promedio_presion = round(sum(self.presiones) / len(self.presiones), 2)
        promedio_viento = round(sum(self.velocidades_viento) / len(self.velocidades_viento), 2)

        direccion_predominante = max(set(self.direcciones_viento), key=self.direcciones_viento.count)

        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_viento, direccion_predominante


archivo_datos = "datos.txt"  
datos = DatosMeteorologicos(archivo_datos)
estadisticas = datos.procesar_datos()

with open("Meteorologia.datos", "w") as resultado:
    resultado.write(f" Temperatura promedio: {estadisticas[0]} °C\n")
    resultado.write(f"Humedad promedio: {estadisticas[1]} %\n")
    resultado.write(f"Presión promedio: {estadisticas[2]} N/m²\n")
    resultado.write(f"Velocidad promedio del viento: {estadisticas[3]} Km/h\n")
    resultado.write(f"Dirección predominante del viento: {estadisticas[4]}")
    
print("Resultados guardados en Meteorologia.datos")