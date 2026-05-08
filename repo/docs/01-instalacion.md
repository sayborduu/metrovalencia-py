# Instalación

Hay varias maneras de instalar `metrovalencia-py`.

## venv
Es recomendable utilizar un entorno virtual para prevenir conflictos con otras librerias o versiones de Python.

```bash
# Crear venv
python -m venv venv
```
activar el venv:
```bash
# Si usas Linux o Mac:
source venv/bin/activate
# Si andas en Windows:
venv\Scripts\activate
```

después de activar el venv puedes instalar el paquete

## desde PyPi (recomendado)

```bash
pip install metrovalencia
```

## Instalar desde el código fuente

```bash
git clone https://github.com/tu-usuario/metrovalencia-py.git
cd metrovalencia-py

pip install -e .
# o
pip install .
```

## Comprobar

```python
import metrovalencia

print(metrovalencia.__version__)
# > 0.1.1
```

## Dependencias
- **httpx** (>=0.24.0)
- **rapidfuzz** (>=3.0.0)