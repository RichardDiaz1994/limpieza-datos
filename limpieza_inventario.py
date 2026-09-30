"""
Proyecto: Limpieza y análisis de datos de inventario (ropa)
Autor: Richard Alexander Diaz Cataño
Descripción: Este script limpia un dataset de inventario con errores típicos
(duplicados, valores nulos, formatos inconsistentes) y genera un dataset
limpio listo para análisis, además de un gráfico simple de cantidades por categoría.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos originales
df = pd.read_csv("inventario_raw.csv")

print("=== ANTES DE LA LIMPIEZA ===")
print(f"Filas totales: {len(df)}")
print(f"Valores nulos por columna:\n{df.isnull().sum()}")
print(f"Filas duplicadas: {df.duplicated(subset=['producto', 'categoria', 'fecha_ingreso']).sum()}")

# 2. Eliminar filas sin nombre de producto (dato crítico faltante)
df = df.dropna(subset=["producto"])

# 3. Eliminar duplicados (mismo producto, categoría y fecha de ingreso)
df = df.drop_duplicates(subset=["producto", "categoria", "fecha_ingreso"])

# 4. Estandarizar texto: quitar espacios extra y poner en formato "Titulo"
df["producto"] = df["producto"].str.strip().str.title()
df["categoria"] = df["categoria"].str.strip().str.title()
df["bodega"] = df["bodega"].str.strip().str.title()

# 5. Reemplazar "N/A" por nulos reales y convertir cantidad a numérico
df["cantidad"] = df["cantidad"].replace("N/A", pd.NA)
df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")

# 6. Rellenar cantidades y precios faltantes con la mediana de su categoría
df["cantidad"] = df.groupby("categoria")["cantidad"].transform(
    lambda x: x.fillna(x.median())
)
df["precio"] = df.groupby("categoria")["precio"].transform(
    lambda x: x.fillna(x.median())
)

# 7. Normalizar las fechas (vienen en varios formatos distintos)
df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"], errors="coerce", format="mixed", dayfirst=True)

# 8. Redondear cantidades a enteros (ya que representan unidades de producto)
df["cantidad"] = df["cantidad"].round().astype(int)

print("\n=== DESPUÉS DE LA LIMPIEZA ===")
print(f"Filas totales: {len(df)}")
print(f"Valores nulos por columna:\n{df.isnull().sum()}")

# 9. Guardar el dataset limpio
df.to_csv("inventario_limpio.csv", index=False)
print("\nArchivo 'inventario_limpio.csv' generado correctamente.")

# 10. Crear un gráfico simple: cantidad total por categoría
resumen = df.groupby("categoria")["cantidad"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
resumen.plot(kind="bar", color="#4C72B0")
plt.title("Cantidad total en inventario por categoría")
plt.xlabel("Categoría")
plt.ylabel("Cantidad (unidades)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("cantidad_por_categoria.png")
print("Gráfico 'cantidad_por_categoria.png' generado correctamente.")
