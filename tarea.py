from datetime import datetime

class Tarea:
    def __init__(self, id_tarea, nombre, descripcion, prioridad, completada: bool = False):
        self.id_tarea = id_tarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.creado_en = datetime.now()
        self.prioridad = prioridad
        self.completada = completada

    def marcar_completada(self):
        self.completada = True
    



