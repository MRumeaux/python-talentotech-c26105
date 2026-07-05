<div align="center">
  <h1>📦 Sistema de Gestión de Inventario</h1>
  <p><strong>Un sistema interactivo en consola desarrollado en Python y SQLite3 para la administración eficiente de productos.</strong></p>

  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite3">
  <img src="https://img.shields.io/badge/Colorama-UI-green?style=for-the-badge" alt="Colorama">
</div>

<hr />

## 📝 Descripción del Proyecto

Este proyecto es una aplicación de terminal modular diseñada para gestionar el inventario de un negocio. Permite realizar todas las operaciones **CRUD** (Crear, Leer, Actualizar, Borrar) sobre una base de datos relacional local, ofreciendo una experiencia visual fluida gracias a la implementación de un menú dinámico y un carrusel de colores por línea de comandos.

---

## 🚀 Características Principales

* **Persistencia Robusta:** Conexión directa a una base de datos local SQLite (`inventario.db`).
* **CRUD Completo de Productos:**
    * `Registrar`: Alta de productos controlando campos obligatorios.
    * `Visualizar`: Lista completa con un **carrusel de colores iterativo** línea por línea para máxima legibilidad.
    * `Buscar`, `Modificar` y `Eliminar`: Operaciones precisas localizadas mediante el `ID` único del producto.
* **Reportes de Alerta:** Módulo de consulta dinámico para filtrar productos con stock crítico (igual o inferior al límite establecido por el usuario).
* **Interfaz Resiliente:** Menú numérico protegido con control de flujo para evitar cierres inesperados ante ingresos de caracteres alfabéticos.

---

## 📂 Estructura del Repositorio

El proyecto se encuentra estrictamente modularizado siguiendo las buenas prácticas de desarrollo:

<table>
  <thead>
    <tr>
      <th>Archivo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>setup_db_y_tabla.py</code></td>
      <td>Script de inicialización. Se encarga de crear la base de datos <code>inventario.db</code> y la tabla <code>productos</code> con sus respectivas restricciones (claves primarias, autoincrementos y campos no nulos).</td>
    </tr>
    <tr>
      <td><code>funciones_aux.py</code></td>
      <td>El núcleo lógico del sistema. Contiene todas las funciones de interacción con la base de datos, captura de datos del terminal y validaciones de negocio.</td>
    </tr>
    <tr>
      <td><code>ejercicio_evolutivo.py</code></td>
      <td>El punto de entrada de la aplicación (Main). Maneja el ciclo de vida del programa a través de un bucle infinito y la estructura moderna <code>match-case</code> para direccionar el menú.</td>
    </tr>
  </tbody>
</table>

---

## 🛠️ Tecnologías y Requisitos

* **Lenguaje:** Python 3.10 o superior.
* **Base de Datos:** SQLite3 (incluido en la librería estándar de Python).
* **Librerías Externas:**
    * `colorama` (para estilizado de fuentes en consola).

---

## ⚙️ Instalación y Ejecución

Sigue estos pasos para clonar y ejecutar el sistema de gestión en tu entorno local:

1. **Clonar el repositorio:**
   ```CMD
   git clone [https://github.com/MRumeaux/python-talentotech-c26105.git]
2. **Instalar dependencias necesarias:**
   ```CMD
   pip install colorama
3. **Inicializar la Base de Datos:**
   Antes de correr el programa por primera vez, genera la estructura de la base de datos ejecutando:
   ```CMD
   python setup_db_y_tabla.py
4. **Iniciar la Aplicación:**
   Lanza el sistema interactivo ejecutando el archivo principal:
   ```CMD
   python ejercicio_evolutivo.py

---

## 📊 Estructura de la Tabla 'productos'

La base de datos modela la entidad bajo los siguientes estándares requeridos:

<ul>
  <li><code>id</code>: INTEGER (Clave primaria, autoincremental).</li>
  <li><code>nombre</code>: TEXT (Obligatorio, no nulo).</li>
  <li><code>descripcion</code>: TEXT (Detalle opcional).</li>
  <li><code>categoria</code>: TEXT (Clasificación del producto).</li>
  <li><code>cantidad</code>: INTEGER (Stock disponible, no nulo).</li>
  <li><code>precio</code>: REAL (Valor monetario, no nulo).</li>
</ul>

<br />

<hr />

### 💡 Detalles de diseño incluidos en este repositorio:
* **Encabezado HTML (`<div align="center">`)**: Centra el título y los logos/badges tecnológicos para darle una estética de repositorio oficial de software.
* **Badges dinámicos**: Muestran las tecnologías usadas con sus colores representativos nativos en GitHub.
* **Tabla HTML (`<table>`)**: Reemplaza las tablas comunes de Markdown por una estructura HTML limpia que se renderiza mejor visualmente en dispositivos móviles y de escritorio.
* **Lista HTML (`<ul>`)**: Utilizada en la sección de la base de datos para mantener sangrías perfectas al detallar tipos de datos del esquema SQL.
