import csv


datos = 'actividades.csv'

# Diccionario para almacenar la duración de cada actividad
duracion_actividades = {}

# Diccionario para almacenar las dependencias de cada actividad
dependencias_actividades = {}

with open(datos, newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    
    for fila in lector_csv:
        nombre_actividad = fila['nombre_actividad']
        duracion = int(fila['duracion'])
        dependencias = fila['dependencias'].split(',') if fila['dependencias'] else []

        duracion_actividades[nombre_actividad] = duracion
        dependencias_actividades[nombre_actividad] = dependencias

# Función para calcular el tiempo más temprano de inicio (TES) de cada actividad
def calcular_tes():
    tes = {}
    for actividad in duracion_actividades.keys():
        if actividad not in tes:
            tes[actividad] = 0
        for dependencia in dependencias_actividades[actividad]:
            tes[actividad] = max(tes[actividad], duracion_actividades[dependencia] + tes[dependencia])
    return tes

# Función para calcular el tiempo más tardío de inicio (TTS) de cada actividad
def calcular_tts(tes):
    tts = {actividad: tes[actividad] for actividad in duracion_actividades.keys()}
    actividades_ordenadas = sorted(duracion_actividades.keys(), key=lambda x: tes[x], reverse=True)
    for actividad in actividades_ordenadas:
        for siguiente_actividad in dependencias_actividades.keys():
            if actividad in dependencias_actividades[siguiente_actividad]:
                tts[actividad] = min(tts[actividad], tts[siguiente_actividad] - duracion_actividades[actividad])
    return tts

# Calcular el tiempo más temprano de inicio (TES)
tes = calcular_tes()

# Calcular el tiempo más tardío de inicio (TTS)
tts = calcular_tts(tes)

# Imprimir los resultados
print("Tiempo más temprano de inicio (TES):")
for actividad, tiempo in tes.items():
    print(f"{actividad}: {tiempo}")

print("\nTiempo más tardío de inicio (TTS):")
for actividad, tiempo in tts.items():
    print(f"{actividad}: {tiempo}")

# Calcular la ruta crítica
ruta_critica = [actividad for actividad in duracion_actividades.keys() if tes[actividad] == tts[actividad]]

print("\nRuta crítica:")
print(ruta_critica)