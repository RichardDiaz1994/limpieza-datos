# Limpieza y Análisis de Datos de Inventario

## 🎯 Objetivo
Limpiar un dataset de inventario de productos (ropa) con errores comunes en datos reales:
valores nulos, filas duplicadas, formatos de fecha inconsistentes y textos con formato irregular.
Luego generar una visualización simple de la cantidad total en inventario por categoría.

## 📂 Dataset
`inventario_raw.csv` — dataset simulado, inspirado en procesos reales de gestión de inventario
de una empresa de confección (materia prima y producto terminado), similar a proyectos en los
que he trabajado profesionalmente.

Columnas:
- `id_producto`: identificador único del producto
- `producto`: nombre del producto
- `categoria`: categoría (ropa superior, inferior, exterior)
- `cantidad`: unidades en inventario
- `precio`: precio unitario (COP)
- `fecha_ingreso`: fecha de ingreso a bodega
- `bodega`: bodega donde se almacena

## 🛠️ Herramientas
- **Python** (pandas, matplotlib)

## 🔧 Proceso de limpieza
1. Eliminación de filas con datos críticos faltantes (producto sin nombre).
2. Eliminación de registros duplicados.
3. Estandarización de texto (mayúsculas/minúsculas inconsistentes, espacios extra).
4. Conversión de valores tipo "N/A" a nulos reales.
5. Relleno de valores numéricos faltantes usando la mediana por categoría.
6. Normalización de fechas (venían en formatos mixtos: `2024-01-15`, `15/01/2024`, `2024/02/15`).
7. Exportación del dataset limpio (`inventario_limpio.csv`).

## 📊 Resultado
- El dataset pasó de 15 filas (con nulos y duplicados) a 13 filas limpias y consistentes.
- Se generó un gráfico (`cantidad_por_categoria.png`) mostrando la cantidad total de
  unidades en inventario por categoría, útil para identificar qué línea de producto
  tiene mayor rotación o volumen.

## 💡 Hallazgos clave
- La categoría "Ropa Superior" concentra la mayor cantidad de unidades en inventario.
- Se detectaron y corrigieron múltiples formatos de fecha, un error común al consolidar
  datos de distintas fuentes o sistemas.
- El 13% de los registros originales tenían algún tipo de inconsistencia (nulos o duplicados).

## 🚀 Cómo ejecutarlo
```bash
pip install pandas matplotlib
python limpieza_inventario.py
```
