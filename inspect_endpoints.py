import inspect
from metrovalencia import MetroValencia

metro = MetroValencia(app_name="test_script", contact="dev@alexbadi.es")

resources = {
    "previsiones": metro.previsiones,
    "paradas": metro.paradas,
    "incidencias": metro.incidencias,
    "tarjetas": metro.tarjetas,
    "rutas": metro.rutas,
    "tarifas": metro.tarifas,
    "comunicaciones": metro.comunicaciones,
    "v2.incidencias": metro.v2.incidencias,
}

for name, resource in resources.items():
    print(f"\n--- {name} ---")
    methods = [func for func in dir(resource) if callable(getattr(resource, func)) and not func.startswith("_")]
    print(", ".join(methods))

metro.close()
