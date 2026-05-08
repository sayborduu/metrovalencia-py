# Documentación

1. **[Instalación](01-instalacion.md)** - Cómo instalar el paquete
2. **[Inicio Rápido](02-inicio-rapido.md)** - Uso básico y primeros pasos
3. **[Recursos](03-recursos.md)** - Métodos y recursos de la API
4. **[Modelos](04-modelos.md)** - Estructura de los datos
5. **[Excepciones](05-excepciones.md)** - Clasificación de errores posibles
6. **[Referencia API](06-referencia.md)** - Información general de la API



## Ejemplo rápido

```python
from metrovalencia import MetroValencia

# Inicialización del cliente
metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com"
)

# Previsiones
previsiones = metro.previsiones.get("Alameda")
print(f"Líneas disponibles: {[p.line for p in previsiones.previsiones]}")

# Búsqueda
paradas = metro.paradas.buscar("Marítim")
print(f"Estaciones: {len(paradas.paradas)}")

# Rutas
ruta = metro.rutas.rutap("Colón", "Bailén")
print(f"Tiempo aproximado: {ruta.tiempo_total_minutos:.2f} minutos")

metro.close()
```

## Licencia

MIT