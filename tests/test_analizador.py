# tests/test_analizador.py
import os
import pytest
import pandas as pd
from src.analizador import (
    cargar_ventas,
    calcular_total_por_producto,
    top_productos,
    ventas_por_mes,
    generar_grafico_barras,
)

# ── Ruta al CSV de prueba ──────────────────────────────────────────────────────
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "ventas.csv")


# ── Fixture: DataFrame reutilizable en todos los tests ────────────────────────
@pytest.fixture
def df_ventas():
    """Carga el CSV real y devuelve un DataFrame listo para los tests."""
    return cargar_ventas(CSV_PATH)


# ── FASE 3.2 — Tests obligatorios ─────────────────────────────────────────────

def test_cargar_ventas_ok(df_ventas):
    """El CSV se carga correctamente y tiene las columnas esperadas."""
    assert isinstance(df_ventas, pd.DataFrame)
    assert set(df_ventas.columns) >= {"producto", "cantidad", "precio_unitario", "mes"}
    assert len(df_ventas) == 9  # 9 filas en nuestro CSV


def test_cargar_ventas_archivo_no_existe():
    """Lanza FileNotFoundError si el archivo no existe."""
    with pytest.raises(FileNotFoundError):
        cargar_ventas("ruta/que/no/existe.csv")


def test_cargar_ventas_columna_faltante(tmp_path):
    """Lanza ValueError si el CSV no tiene todas las columnas obligatorias."""
    csv_incompleto = tmp_path / "incompleto.csv"
    csv_incompleto.write_text("producto,cantidad\nManzanas,10\n")
    with pytest.raises(ValueError):
        cargar_ventas(str(csv_incompleto))


def test_calcular_total_manzanas(df_ventas):
    """El total de Manzanas es: 50×1.20 + 40×1.25 + 60×1.30 = 60+50+78 = 188."""
    totales = calcular_total_por_producto(df_ventas)
    assert totales["Manzanas"] == pytest.approx(188.0)


def test_top_productos_n2(df_ventas):
    """Devuelve exactamente 2 productos cuando n=2."""
    resultado = top_productos(df_ventas, n=2)
    assert len(resultado) == 2
    assert isinstance(resultado, list)


def test_ventas_por_mes_enero(df_ventas):
    """
    Total enero = (50×1.20) + (30×0.90) + (80×0.60)
                =   60.00  +   27.00  +   48.00  = 135.0
    """
    por_mes = ventas_por_mes(df_ventas)
    assert por_mes["enero"] == pytest.approx(135.0)


def test_generar_grafico_crea_archivo(df_ventas, tmp_path):
    """El PNG se genera en disco."""
    ruta = str(tmp_path / "grafico.png")
    generar_grafico_barras(df_ventas, ruta)
    assert os.path.exists(ruta)
    assert os.path.getsize(ruta) > 0


# ── Tests extra para asegurar cobertura ≥ 80% ─────────────────────────────────

def test_top_productos_default(df_ventas):
    """Sin pasar n, devuelve los 3 mejores por defecto."""
    resultado = top_productos(df_ventas)
    assert len(resultado) == 3


def test_ventas_por_mes_devuelve_series(df_ventas):
    """ventas_por_mes devuelve una pd.Series con los 3 meses."""
    resultado = ventas_por_mes(df_ventas)
    assert isinstance(resultado, pd.Series)
    assert "febrero" in resultado.index
    assert "marzo" in resultado.index


def test_calcular_total_por_producto_devuelve_series(df_ventas):
    """calcular_total_por_producto devuelve una pd.Series."""
    resultado = calcular_total_por_producto(df_ventas)
    assert isinstance(resultado, pd.Series)
    assert "Plátanos" in resultado.index
    assert "Naranjas" in resultado.index