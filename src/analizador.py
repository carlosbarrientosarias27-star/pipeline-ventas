# src/analizador.py
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # modo sin pantalla (necesario en el pipeline)
import matplotlib.pyplot as plt

COLUMNAS_OBLIGATORIAS = {"producto", "cantidad", "precio_unitario", "mes"}


def cargar_ventas(ruta_csv: str) -> pd.DataFrame:
    """Carga el CSV y devuelve un DataFrame.
    Lanza FileNotFoundError si el archivo no existe.
    Lanza ValueError si le faltan columnas obligatorias."""
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")
    
    df = pd.read_csv(ruta_csv)
    
    columnas_faltantes = COLUMNAS_OBLIGATORIAS - set(df.columns)
    if columnas_faltantes:
        raise ValueError(f"Faltan columnas obligatorias: {columnas_faltantes}")
    
    return df


def calcular_total_por_producto(df: pd.DataFrame) -> pd.Series:
    """Devuelve Series con el total (cantidad × precio_unitario) por producto."""
    df = df.copy()
    df["total"] = df["cantidad"] * df["precio_unitario"]
    return df.groupby("producto")["total"].sum()


def top_productos(df: pd.DataFrame, n: int = 3) -> list:
    """Devuelve lista con los n productos con mayor total de ventas."""
    totales = calcular_total_por_producto(df)
    return totales.sort_values(ascending=False).head(n).index.tolist()


def ventas_por_mes(df: pd.DataFrame) -> pd.Series:
    """Devuelve Series con el total de ventas agrupado por mes."""
    df = df.copy()
    df["total"] = df["cantidad"] * df["precio_unitario"]
    return df.groupby("mes")["total"].sum()


def generar_grafico_barras(df: pd.DataFrame, ruta_salida: str) -> None:
    """Genera gráfico de barras con ventas por producto y lo guarda en ruta_salida."""
    totales = calcular_total_por_producto(df)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    totales.plot(kind="bar", ax=ax, color=["#e74c3c", "#f39c12", "#2ecc71"])
    ax.set_title("Ventas totales por producto")
    ax.set_xlabel("Producto")
    ax.set_ylabel("Total (€)")
    ax.tick_params(axis="x", rotation=0)
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close(fig)