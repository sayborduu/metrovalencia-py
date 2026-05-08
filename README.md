<div align="center">

<img
  src="./repo/Icon.ico"
  alt="Picture"
  style="height: 130px; border-radius: 20px;"
/>

# metrovalencia-py

  <a href="https://github.com/sayborduu/metrovalencia-py/stargazers">
    <img src="https://img.shields.io/github/stars/sayborduu/metrovalencia-py?style=flat&logo=github" alt="GitHub stars">
  </a>
  <a href="https://github.com/sayborduu/metrovalencia-py/releases">
    <img src="https://img.shields.io/github/v/release/sayborduu/metrovalencia-py?style=flat&logo=github" alt="GitHub release">
  </a>

  Este es un paquete de Python para sacar datos de Metrovalencia usando MetroAPI (la API no oficial).

<a href="https://dash.metroapi.alexbadi.es">panel API</a>
•
[documentación](repo/docs/README.md)
•
<a href="https://docs.metroapi.alexbadi.es">documentación MetroAPI</a>


</div>

## Un vistazo rápido

```python
from metrovalencia import MetroValencia

metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com"
)

previsiones = metro.previsiones.get("Alameda")
for p in previsiones.previsiones:
    print(f"Línea {p.line} va a {p.destino} y llega en {p.seconds}s")

result = metro.paradas.buscar("Marítim")
print(f"He encontrado {len(result.paradas)} paradas")

ruta = metro.rutas.rutap("Colón", "Bailén")
print(f"Vas a tardar como {ruta.tiempo_total_minutos:.2f} minutillos")

metro.close()
```

## Documentación

Puedes ver la documentación en **[repo/docs/README.md](repo/docs/README.md)**.

## Datos

Puedes elegir el formato de las respuestas usando `response_type`. Hay tres opciones:

- **`class`** (por defecto): Datos en `dataclasses`
- **`json`**: Respuesta exacta del servidor.
- **`parsed_json`**: JSON pero más limpio (se quitan los `null` y se utiliza `snake_case`).

```python
metro = MetroValencia(
    app_name="miapp",
    contact="dev@ejemplo.com",
    response_type="class"  # por defecto
)
```

## ¿Qué puedes hacer?

- Puedes ver previsiones o el estado de las paradas
- Ver las incidencias de transporte o accesibilidad
    - Ver incidencias v2, en pruebas, basadas en los Tweets y Incidencias de la API, categorizadas con IA.
- Ver información de tarjetas de metro
- Hacer rutas entre dos paradas
- Información, como las tarifas, zonas
- Obtener las noticias de metrovalencia


## Historial de Estrellas

<a href="https://www.star-history.com/?repos=sayborduu%2Fmetrovalencia-py&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=sayborduu/metrovalencia-py&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=sayborduu/metrovalencia-py&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=sayborduu/metrovalencia-py&type=date&legend=top-left" />
 </picture>
</a>

## Licencia
MIT