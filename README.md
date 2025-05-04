# Gestor de Tareas CLI

Un gestor de tareas simple en línea de comandos que te permite organizar tus tareas diarias.

## Características

- Añadir nuevas tareas
- Listar todas las tareas o filtrar por estado
- Actualizar el contenido de una tarea
- Eliminar tareas
- Marcar tareas como "en progreso" o "completadas"
- Almacenamiento persistente en archivo CSV

## Uso

El programa se ejecuta desde la línea de comandos con los siguientes comandos:

### Añadir una tarea
```bash
python main.py add "Descripción de la tarea"
```

### Listar tareas
```bash
# Listar todas las tareas
python main.py list

# Filtrar tareas por estado
python main.py list todo
python main.py list in-progress
python main.py list done
```

### Actualizar una tarea
```bash
python main.py update ID "Nueva descripción de la tarea"
```

### Eliminar una tarea
```bash
python main.py delete ID
```

### Cambiar estado de una tarea
```bash
# Marcar como en progreso
python main.py mark-in-progress ID

# Marcar como completada
python main.py mark-done ID
```

## Estructura de Datos

Las tareas se almacenan en un archivo CSV con la siguiente estructura:
- ID: Identificador único de la tarea
- Descripción: Texto de la tarea
- Estado: Puede ser "todo", "in-progress" o "done"
- Fecha de creación: Timestamp de cuando se creó la tarea
- Fecha de última modificación: Timestamp de la última actualización

## Requisitos

- Python 3.x
- Módulos estándar de Python (sys, csv, datetime)

## Notas

- El archivo de tareas se guarda como `tasks.csv` en el directorio actual
- Cada tarea tiene un ID único que se incrementa automáticamente
- Las fechas se guardan en formato "YYYY-MM-DD HH:MM:SS"


https://roadmap.sh/projects/task-tracker