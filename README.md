# 📚 Proyecto de Gestión de Biblioteca con Flask, MySQL y MongoDB

## 📝 Introducción

Este proyecto es una aplicación web de gestión de biblioteca que permite realizar operaciones **CRUD (Create, Read, Update, Delete)** tanto en **MySQL** como en **MongoDB**. Su objetivo principal es administrar libros y usuarios mediante una interfaz intuitiva con **Bootstrap** en un estilo oscuro y formal.

## 🚀 Funcionalidades

### 📖 Libros

- Agregar libros mediante un formulario.
- Mostrar los libros en una tabla con opciones de edición y eliminación.
- Búsqueda por nombre, autor o ISBN.
- Confirmación antes de actualizar o eliminar un libro.

### 👥 Usuarios

- Registrar usuarios en el sistema.
- Mostrar los usuarios en una tabla.
- Búsqueda por nombre o correo electrónico.

### 🎨 Diseño

- Interfaz con **Bootstrap** en estilo oscuro y formal.

---

## 📂 Estructura del Proyecto

```
Bibl-Python-MySQL/
│── app.py                # Archivo principal de Flask  
│── config.py             # Configuración de MySQL  
│── static/               # Archivos estáticos (CSS, JS, imágenes)  
│── templates/            # Plantillas HTML  
│── routes.py             # Módulo con las rutas de la aplicación   
│── models.py             # Modelos para interactuar con la base de datos   
│── README.md             # Este archivo  
│── _pycache_/            # Archivos caché generados por Python  
│── venv/                 # Entorno virtual  
│── .gitignore            # Archivos y carpetas a excluir en Git  
```

---

## 🛠 Instalación y Configuración

### 🔧 Herramientas utilizadas

- **Flask** para la creación de la aplicación web.
- **Flask-MySQL**, **Flask-SQLAlchemy** para la integración con MySQL.
- **Flask-PyMongo** para la integración con MongoDB.
- **Mensajes Flask** para notificaciones en la aplicación.
- **Bootstrap** para el diseño de la interfaz.

### 🏗️ Configuración del entorno

1️⃣ **Clonar el repositorio**

```sh
 git clone https://github.com/tu-usuario/Bibl-Python-MySQL.git
 cd Bibl-Python-MySQL
```

2️⃣ **Crear y activar un entorno virtual**

```sh
python -m venv venv  
# En Windows:
venv\Scripts\activate  
# En macOS/Linux:
source venv/bin/activate
```

🔹 *El entorno virtual permite instalar dependencias sin afectar el sistema global.*

3️⃣ **Instalar dependencias**

```sh
pip install flask flask-mysql flask-sqlalchemy flask-pymongo flask
```

4️⃣ **Ejecutar la aplicación**

```sh
python app.py
```

📌 La aplicación estará disponible en: `http://127.0.0.1:5000/`

---

## 📊 Diagramas

🖼️ **Diagrama de Casos de Uso**

> ![Diagrama de Casos de Uso](statics/Diagrama_de_casos_de_uso.png)


🖼️ **Diagrama de Clases**

> ![Diagrama de Clases](statics/Diagrama_de_clases.png)

🖼️ **Diagrama de Entidad-Relación**

> ![Diagrama de Clases](statics/Diagrama_Entidad-Relacion.png)
---

## 📌 Versionado de las Bases de Datos

- **MySQL Community Server** 9.2.0 Innovation
- **MySQL Workbench** 8.0.41
- **MongoDB** 8.0.4
- **MongoDB Compass** 1.45.4

---

## ✒️ Autores

- **Luis Esteban Rodríguez Muñoz**

---

## 🎁 Expresiones de Gratitud

Un agradecimiento especial a:

- **Juan Pablo Jiménez**
- **ChatGPT** por su ayuda en la documentación ✨

📌 ¡Si te gusta este proyecto, te dejo mi cuenta Nequi: 3137914016 para apoyar la causa !

