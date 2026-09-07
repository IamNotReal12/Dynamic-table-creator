# Dynamic-table-creator
<h1 align="center">🗄️ Gestor de Tablas Dinámicas - Academic SQL</h1>

<p align="center">
  Aplicación de escritorio desarrollada en Python para la gestión interactiva de bases de datos SQLite, estructuración dinámicas de tablas y exportación de datos, construida con CustomTkinter.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/CustomTkinter-00599C?style=for-the-badge&logo=python&logoColor=white" alt="CustomTkinter"/>
</p>

---

## ✨ Características Principales

- 🏗️ **Creación Dinámica de Tablas:** Permite inicializar y estructurar tablas personalizadas en SQLite (`BaseDatos.db`) orientadas a gestión de datos y registros (socios, planes, pesos, proteínas, asistencias).
- 📝 **Inserción de Registros:** Ventana modal interactiva (*Toplevel*) para agregar nuevos datos de forma limpia y controlada.
- 🔄 **Actualización en Tiempo Real:** Modificación rápida de campos específicos mediante el ID del registro y consultas `UPDATE` automatizadas.
- 🗑️ **Gestión y Limpieza de Tablas:** Opción para eliminar tablas completas (`DROP TABLE`) y reiniciar secuencias de autoincremento.
- 💾 **Exportación a CSV:** Funcionalidad para guardar el contenido visualizado de la tabla directamente en un archivo `.csv` con compatibilidad de codificación utf-8.

---

## 🛠️ Requisitos e Instalación

1. **Asegúrate de tener Python instalado junto con las dependencias requeridas:**
   ```bash
   pip install customtkinter CTkTable
2.python DataBase.py   
