![alt logoFiusac](Logo.png)

# Manual Técnico - Sistema de Transporte LlegaRapidito

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Estructuras de Datos](#estructuras-de-datos)
4. [Detalles de Implementación](#detalles-de-implementación)
5. [Algoritmos](#algoritmos)
6. [Requerimientos Técnicos](#requerimientos-técnicos)

## Introducción

LlegaRapidito Transportation System es una solución integral de gestión de transporte desarrollada en Python utilizando el framework GUI Tkinter. El sistema está diseñado para gestionar de manera eficiente flotas de vehículos, información de clientes, rutas y logística de viajes a través de estructuras de datos y algoritmos optimizados.

### Propósito

El sistema tiene como objetivo proporcionar una solución robusta para:

- Gestión de información de clientes
- Control de flota de vehículos
- Optimización de rutas
- Seguimiento de logística de viajes
- Análisis de rendimiento y generación de informes

## Arquitectura del Sistema

### Stack Tecnológico

- **Lenguaje de Programación:** Python
- **Framework GUI:** Tkinter
- **Visualización:** Graphviz
- **Almacenamiento de Datos:** Estructuras de datos en memoria

### Componentes Principales

1. Módulo de Gestión de Clientes
2. Módulo de Gestión de Vehículos
3. Módulo de Gestión de Rutas
4. Módulo de Logística de Viajes
5. Sistema de Reportes

## Estructuras de Datos

### 1. Lista Circular Doblemente Enlazada

```python
class circular_doubly_linked:
    def __init__(self):
        self.head = None
```

Utilizada para la gestión de clientes, esta estructura proporciona:

- Recorrido bidireccional eficiente
- Capacidades de navegación circular
- Complejidad de búsqueda O(n)
- Óptima para inserciones y eliminaciones frecuentes

Operaciones principales:

- Insertar: O(n)
- Eliminar: O(n)
- Buscar: O(n)
- Actualizar: O(n)

### 2. Árbol B

```python
class bTree:
    def __init__(self, order: int):
        self.root = BTreeNode(True)
        self.order: int = order
```

Implementa la gestión de vehículos con:

- Estructura de árbol B de orden 5
- Propiedades de árbol balanceado
- Operaciones de búsqueda eficientes
- Capacidades de auto-balanceo

Operaciones principales:

- Insertar: O(log n)
- Buscar: O(log n)
- Eliminar: O(log n)
- Actualizar: O(log n)

### 3. Lista de Adyacencia (Grafo)

```python
class adjacency_list:
    def __init__(self):
        self.vertices: linked_list = linked_list()
```

Gestiona la información de rutas con:

- Representación flexible de grafos
- Recorrido eficiente de aristas
- Gestión dinámica de rutas
- Óptimo para grafos dispersos

Operaciones principales:

- Agregar vértice: O(1)
- Agregar arista: O(1)
- Encontrar vértice: O(V)
- Recorrer aristas: O(E)

### 4. Algoritmo de Ruta Más Corta

```python
class shortest_path:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list
```

Implementa la optimización de rutas con:

- Adaptación del algoritmo de Dijkstra
- Búsqueda de caminos basada en prioridad
- Cálculo eficiente de rutas
- Capacidades de seguimiento de caminos

Características de rendimiento:

- Complejidad temporal: O(V + E log V)
- Complejidad espacial: O(V)

## Detalles de Implementación

### Gestión de Clientes

La implementación de lista circular doblemente enlazada proporciona:

- Recorrido bidireccional para búsqueda eficiente de clientes
- Estructura circular para iteración continua
- Asignación dinámica de memoria para escalabilidad
- Mantiene orden por DPI del cliente

### Gestión de Flota de Vehículos

La implementación del árbol B ofrece:

- Estructura de árbol balanceada para rendimiento consistente
- Consultas de rango eficientes
- Rebalanceo automático
- Optimizado para patrones de acceso

### Gestión de Rutas

La estructura de grafo de lista de adyacencia permite:

- Representación flexible de rutas
- Búsqueda eficiente de caminos
- Actualizaciones dinámicas de rutas
- Almacenamiento eficiente en memoria

## Algoritmos

### Optimización de Rutas

El algoritmo de ruta más corta implementa:

1. Selección de nodos basada en prioridad
2. Seguimiento de distancias
3. Reconstrucción de caminos
4. Optimización para restricciones de tiempo

```python
def find_shortest_path(self, start: str, end: str):
    unvisited = path_list_node()
    path_tracker = path_list_node()
    unvisited.insert(start, 0, "")
```

### Visualización de Datos

- Integración con Graphviz para visualización de estructuras
- Actualizaciones de grafos en tiempo real
- Múltiples formatos de salida (PNG, PDF)
- Opciones de estilo personalizadas

## Requerimientos Técnicos

### Requisitos del Sistema

- Python 3.x
- Biblioteca Graphviz
- Tkinter (incluido en la biblioteca estándar de Python)
- Mínimo 4GB RAM recomendado

### Entorno de Desarrollo

- IDE con soporte para Python
- Instalación de Graphviz
- Git para control de versiones
- Entorno virtual recomendado

### Consideraciones de Rendimiento

- Óptimo para conjuntos de datos hasta 100,000 registros
- El uso de memoria escala con el tamaño de los datos
- El procesamiento de visualización puede impactar el rendimiento
- Considerar procesamiento por lotes para grandes conjuntos de datos
