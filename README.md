# 🛒 Pipeline de Ventas

Sistema automatizado de análisis y procesamiento de datos de ventas con pipeline CI/CD integrado.

# 📋 Descripción

**Pipeline-Ventas** es una herramienta de análisis de datos de ventas que automatiza el procesamiento, validación y generación de reportes a partir de archivos CSV. Incluye un pipeline de integración continua que ejecuta pruebas automáticamente en cada cambio del código.

# 🗂️ Estructura del Proyecto

```
pipeline-ventas/
├── .github/
│   └── workflows/
│       └── pipeline.yml        # Pipeline CI/CD (GitHub Actions)
├── .qodo/
│   ├── agents/                 # Agentes de IA para asistencia al desarrollo
│   └── workflows/              # Flujos de trabajo automatizados
├── data/
│   └── ventas.csv              # Datos de ventas para análisis
├── src/
│   └── analizador.py           # Módulo principal de análisis de ventas
├── tests/
│   └── test_analizador.py      # Tests unitarios del analizador
├── conftest.py                 # Configuración global de pytest
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                  # Archivos ignorados por Git
└── README.md                   # Este archivo
```

# 🚀 Instalación

## Requisitos previos

- Python 3.8+
- pip

## Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/pipeline-ventas.git
   cd pipeline-ventas
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   # En Linux/macOS:
   source venv/bin/activate
   # En Windows:
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

# ▶️ Uso

## Ejecutar el analizador

```bash
python src/analizador.py
```

El analizador procesará el archivo `data/ventas.csv` y generará un reporte con las métricas principales de ventas.

## Formato del CSV de ventas

El archivo `data/ventas.csv` debe contener los datos de ventas con las columnas esperadas por el analizador. Ejemplo:

```csv
fecha,producto,cantidad,precio_unitario,vendedor
2024-01-15,ProductoA,10,25.00,Juan
2024-01-16,ProductoB,5,50.00,María
```

# 🧪 Tests

Ejecuta los tests unitarios con:

```bash
pytest tests/
```

Para ver la cobertura de código:

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

# ⚙️ Pipeline CI/CD

El proyecto incluye un pipeline de GitHub Actions (`.github/workflows/pipeline.yml`) que se ejecuta automáticamente en cada `push` o `pull request` a la rama principal.

El pipeline realiza las siguientes comprobaciones:

1. **Instalación de dependencias** — instala todo lo definido en `requirements.txt`
2. **Ejecución de tests** — corre la suite completa con `pytest`
3. **Validación de datos** — verifica que el CSV de ventas sea procesable

# 🤖 Integración con Qodo

El directorio `.qodo/` contiene la configuración de [Qodo](https://www.qodo.ai/), una herramienta de asistencia al desarrollo con IA que ayuda a:

- Generar y revisar tests automáticamente
- Sugerir mejoras en el código
- Automatizar flujos de trabajo repetitivos

# 📦 Dependencias

Las dependencias principales se encuentran en `requirements.txt`. Típicamente incluyen:

- `pandas` — manipulación y análisis de datos
- `pytest` — framework de testing
- `pytest-cov` — cobertura de tests

# 🤝 Contribución

1. Haz un fork del repositorio
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Haz commit de tus cambios: `git commit -m 'feat: añadir nueva funcionalidad'`
4. Sube la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

# 📄 Licencia

Este proyecto está bajo la licencia especificada en el archivo [LICENSE](LICENSE).

---

> Desarrollado con ❤️ y automatización 🤖