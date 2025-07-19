# Sistema de Apoyos (Pilas y Colas)

**Nombre:** Jorge de Jesus Priego Zapata

**Grupo y materia:** 8vo Semestre - Estrctura de Datos

**Docente** Kevin David Molina Cruz


## Descripción
Sistema web sencillo en Python usando Flask para gestionar:
- **Cola:** Entrega de tarjetas de apoyo (personas esperando su tarjeta).
- **Pila:** Historial de apoyos recibidos (simula deshacer apoyos).

## Estructura del proyecto
```
menuflask/
├── app.py
├── README.md
├── models/
│   ├── pila.py
│   └── cola.py
├── templates/
│   ├── menu.html
│   ├── cola.html
│   └── pila.html
```

## Instrucciones para instalar dependencias y ejecutar
1. Instala Flask:
   ```bash
   pip install flask
   ```
2. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
3. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

## Ejemplo de uso
- Ve a "Entregar Tarjetas (Cola)" para agregar personas a la cola y atenderlas.
- Ve a "Historial de Apoyos (Pila)" para agregar apoyos y deshacer el último.

## Guía visual de uso (3 pasos)

### Paso 1: Menú General
![Menú General](ruta1.png)
Desde el menú principal puedes elegir entre gestionar la **Cola** o el **Historial de Apoyos (Pila)**.

### Paso 2: Cola de Tarjetas
![Cola de Tarjetas](ruta2.png)
En la sección de **Cola** puedes agregar personas y atenderlas en orden de llegada.

### Paso 3: Historial de Apoyos (Pila)
![Historial de Apoyos](ruta3.png)
En la sección de **Pila** puedes agregar apoyos recibidos y deshacer el último si es necesario.

---
