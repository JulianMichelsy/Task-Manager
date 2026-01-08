from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.siguiente_id = 1
        self.tareas = []

    def crear(self, nombre, descripcion, prioridad): 
        tarea = Tarea(nombre=nombre, descripcion=descripcion, prioridad=prioridad, id_tarea=self.siguiente_id)
        self.tareas.append(tarea)
        self.siguiente_id += 1

    def listar(self, filtro):
        if filtro == "completada":
            tareas_filtradas = [t for t in self.tareas if t.completada]

        elif filtro == "pendiente":
            tareas_filtradas = [t for t in self.tareas if not t.completada]
        
        else:
            tareas_filtradas = [t for t in self.tareas]
        
        return tareas_filtradas

    def buscar_id(self, id_objetivo: int):
        for t in self.tareas:
            if id_objetivo == t.id_tarea:
                return t
        return None

    def actualizar(self, id_objetivo: int, nuevo_nombre = None, nueva_desc = None, nueva_prio = None):
        tarea_objetivo = self.buscar_id(id_objetivo)
        if tarea_objetivo is not None:
            if nuevo_nombre is not None:
                tarea_objetivo.nombre = nuevo_nombre
            
            if nueva_desc is not None:
                tarea_objetivo.descripcion = nueva_desc

            if nueva_prio is not None:
                tarea_objetivo.prioridad = nueva_prio
            
            return True
        
        else:
            return False
        
    def eliminar(self, id_objetivo):
        tarea_objetivo = self.buscar_id(id_objetivo)
        if tarea_objetivo is not None:
            self.tareas.remove(tarea_objetivo)
            return True
            
        else:
            return False
            


    
                
                
                
            


                





