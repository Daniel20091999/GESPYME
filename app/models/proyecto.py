from worker_user import Worker_User
from manager_user import Manager_User
from tarea import Tarea

class Proyecto:
    #definimos un metodo constructor
    def __init__(self, id_proyecto : str, nombre_proyecto : str, manager_proyecto : object, empleados : list, tareas : list):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.manager_proyecto = manager_proyecto
        self.empleados = empleados
        self.tareas = tareas

    #definimos una lista donde se guardarán todos los proyectos
    lista_proyectos = []
    
    #definimos un método para mostrar la información básica de los proyectos
    def mostrar_info_basica_proyecto(self):
        print(f"ID: {self.id_proyecto}\nNombre: {self.nombre_proyecto}")
    
    #definimos un metodo para mostrar toda la informacion de un proyecto
    def mostrar_info_completa_proyecto(self):
        print(f"ID: {self.id_proyecto}")
        print(f"Nombre: {self.nombre_proyecto}")
        print(f"Manager: {self.mostrar_manager_proyecto(self.id_proyecto)}")
        print(f"\nTrabajadores: {self.mostrar_trabajadores_proyecto(self.id_proyecto)}\nTareas: {self.mostrar_tareas_proyecto(self.id_proyecto)}")
    
    #definimos un metodo para ostrar todos los proyectos
    @classmethod
    def mostrar_proyectos(cls):
        if len(cls.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            for proyecto in cls.lista_proyectos:
                proyecto.mostrar_info_basica_proyecto()
                
    #definimos un metodo para agregar un empleado a un proyecto
    @classmethod
    def agregar_empleado_a_proyecto(cls, id_proyecto):
        for proyecto in cls.lista_proyectos:
            if proyecto.id_proyecto == id_proyecto:
                print("Lista de trabajadores: ")
                Worker_User.lista_workers()
                while True:
                    id_worker = input("Ingrese el ID del trabajador que desea añadir: ")
                    for worker in Worker_User.lista_workers:
                        if worker.id_worker == id_worker:
                            proyecto.empleados.append(worker)
                            #aumentamos el contador de proyectos del trabajador
                            worker.contador_proyectos_worker += 1
                            print("Trabajador añadido correctamente")
                            opcion = input("¿Desea añadir otro trabajador? (s/n): ")
                            if opcion.lower() == "n":
                                break


    #definimos un metodo para eliminar un empleado a un proyecto
    @classmethod
    def eliminar_empleado_a_proyecto(cls, id_proyecto):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    print("Lista de trabajadores: ")
                    Worker_User.lista_workers()
                    while True:
                        id_worker = input("Ingrese el ID del trabajador que desea eliminar: ")
                        for worker in proyecto.empleados:
                            if worker.id_worker == id_worker:
                                #disminuimos el contador de proyectos del trabajador
                                worker.contador_proyectos_worker -= 1
                                proyecto.empleados.remove(worker)
                                print("Trabajador eliminado correctamente")
                                opcion = input("¿Desea eliminar otro trabajador? (s/n): ")
                                if opcion == "n":
                                    break
                                
    #definimos un metodo para asignar un manager a un proyecto
    @classmethod
    def asignar_manager_a_proyecto(cls,id_proyecto):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    print("Lista de managers: ")
                    Manager_User.lista_managers()
                    id_manager = input("Ingrese el ID del manager que desea añadir: ")
                    for manager in Manager_User.lista_managers:
                        if manager.id_manager == id_manager:
                            proyecto.manager_proyecto = manager
                            #aumentamos el contador de proyectos del trabajador
                            manager.contador_proyectos_manager += 1
                            print("Manager asignado correctamente")

    #definimos un metodo para desasignar un manager a un proyecto
    @classmethod
    def desasignar_manager_a_proyecto(cls, id_proyecto):
        if len(Proyecto.lista_proyectos) == 0:
            print("No existen proyectos")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    id_manager = proyecto.manager_proyecto.id_manager
                    for manager in Manager_User.lista_managers:
                        if manager.id_manager == id_manager:
                            proyecto.manager_proyecto = manager
                            #aumentamos el contador de proyectos del trabajador
                            manager.contador_proyectos_manager += 1
                            proyecto.manager_proyecto = None                   
        
    #definimos un metodo para asignar una tarea a un proyecto
    @classmethod
    def asignar_tarea_a_proyecto(cls, id_proyecto):
        if Tarea.lista_tareas == 0:
            print("No hay tareas")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    while True:
                        print("Estas son las tareas disponibles que no se han asignado a ningun proyecto")
                        for tarea in Tarea.lista_tareas:
                            if tarea.id_proyecto != "":
                                tarea.mostrar_informacion_basica_tarea()
                                id_tarea = str("Introduce el id de la tarea que quieres asignar: ")
                                for tarea in Tarea.lista_tareas:
                                    if tarea.id_tarea == id_tarea:
                                        proyecto.tareas.appendd(tarea)
                                        #asignamos el valor del id proyecto a la tarea que se va a asignar
                                        tarea.id_proyecto = id_proyecto
                                        print("Tarea asignada correctamente")
                                        opcion = str("¿Quieres asignar otra tarea? (s/n): ")
                                        if opcion.lower() == "n":
                                            break
                            else:
                                print("no existe una tarea con ese id")             
        
    #definimos un metodo para desasignar una tarea a un proyecto
    @classmethod
    def desasignar_tarea_a_proyecto(cls, id_proyecto):
        if Tarea.lista_tareas == 0:
            print("No hay tareas")
        else:
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_proyecto:
                    while True:
                        print("Estas son las tareas de este proyecto")
                        for tarea in Tarea.lista_tareas:
                            if tarea.id_proyecto == id_proyecto:
                                tarea.mostrar_informacion_basica_tarea()
                                id_tarea = str("Introduce el id de la tarea que quieres desasignar: ")
                                for tarea in Tarea.lista_tareas:
                                    if tarea.id_tarea == id_tarea:
                                        proyecto.tareas.remove(tarea)
                                        #Quitamos la asignacion del proyecto en la tarea
                                        tarea.id_proyecto = ""
                                        print("Tarea desasignada correctamente")
                                        opcion = str("¿Quieres desasignar otra tarea? (s/n): ")
                                        if opcion.lower() == "n":
                                            break
                            else:
                                print("no existe una tarea con ese id")    
    
     #definimos un metodo para crear un nuevo proyecto
    @classmethod
    def crear_proyecto(cls):
        #creamos la lista de empleados del proyecto vacia
        empleados = []
        #creamos la lista de tareas del proyecto vacia
        tareas = []
        if len(cls.lista_proyectos) == 0:
           numero_proyecto = 1
           id_proyecto = "P" + str(numero_proyecto)
        else:
            numero_proyecto = len(cls.lista_proyectos) +1
            id_proyecto = "P" + str(numero_proyecto)
        nombre_proyecto = str(input("Introduce el nombre del proyecto: "))
        if cls.comprobar_nombre_proyecto(nombre_proyecto) == True:
            print("El nombre del proyecto ya existe")
        else:
            print("Lista de managers: ")
            Manager_User.mostrar_managers()
            id_manager = input("Ingrese el ID del manager que desea asignar al proyecto: ")
            for manager in Manager_User.lista_managers:
                if manager.id_manager == id_manager:
                    #aumentamos el contador de proyectos del trabajador
                    manager.contador_proyectos_manager += 1
            print("Lista de trabajadores: ")
            Worker_User.mostrar_workers()
            while True:
                id_worker = input("Ingrese el ID del trabajador que desea añadir: ")
                for worker in Worker_User.lista_workers:
                    if worker.id_worker == id_worker:
                        empleados.append(worker)
                        print("Trabajador asignado correctamente al proyecto")
                        #aumentamos el contador de proyectos del trabajador
                        worker.contador_proyectos_worker += 1
                        opcion = input("¿Desea añadir otro trabajador? (s/n): ")
                        if opcion.lower() == "n":
                            break
                break           
        #creamos el objeto proyecto
        proyecto = Proyecto(id_proyecto, nombre_proyecto, manager, empleados, tareas)
        #añadimos el proyecto a la lista de proyectos
        cls.lista_proyectos.append(proyecto)
        print("Proyecto creado correctamente")
                                    
    #definimos un método para eliminar un proyecto en funcion de su ID
    @classmethod
    def eliminar_proyecto(cls):
        if len(cls.lista_proyectos) == 0:
            print("No hay proyectos")
        else:
            id_a_eliminar = str("Introduce el id del proyecto a eliminar o cancelar para volver al menu: ")
            if id_a_eliminar.lower() != "cancelar":
                for proyecto in cls.lista_proyectos:
                    if proyecto.id_proyecto == id_a_eliminar:
                        if cls.comprobar_tareas_proyecto(proyecto.id_proyecto) == True:
                            print("El proyecto tiene tareas, no se puede eliminar")
                        else:
                            confirmar_eliminacion = str(input("¿estas seguro de que quiere eliminar el proyecto? (S/N): "))
                            if confirmar_eliminacion.lower() == "s":
                                #eliminamos el proyecto de la lista de proyectos
                                cls.lista_proyectos.remove(proyecto)
                                print("Proyecto eliminado")
                            else:
                                print("El proyecto no se ha eliminado correctamente")
                    else:
                        print("El proyecto no existe")
            else:
                print("Volviendo al menu")
        
    #definimos un metodo para editar un proyecto
    @classmethod
    def editar_proyecto(cls):
        if len(cls.lista_proyectos) == 0:
            print("No hay proyectos")
        else:
            print("Proyectos actuales")
            cls.mostrar_proyectos()
            id_a_modificar = str(input("Introduce el ID del Proyecto que quieres modificar: "))
            for proyecto in cls.lista_proyectos:
                if proyecto.id_proyecto == id_a_modificar:
                    proyecto.mostrar_info_completa_proyecto()
                    print("¿Que quieres modificar del proyecto?")
                    print("-. 1 Nombre")
                    print("-. 2 Manager")
                    print("-. 3 Trabajadores")
                    print("-. 4 Tareas")
                    print("-. 5 Cancelar")
                    opcion = int(input("que quieres modificar (1-5): "))
                    if opcion == 1:
                        nuevo_nombre = str("Introduce el nuevo nombre del proyecto: ")
                        if proyecto.comprobar_nombre_proyecto(nuevo_nombre) == True:
                            print("El nombre del proyecto ya existe")
                        else:
                            proyecto.nombre_proyecto = nuevo_nombre
                    elif opcion == 2:
                        if proyecto.manager_proyecto != None:
                            proyecto.desasignar_manager_a_proyecto(id_a_modificar)
                        else:
                            proyecto.asignar_manager_a_proyecto(id_a_modificar)
                    elif opcion == 3:
                        if len(proyecto.trabajadores) == 0:
                            print("No hay trabajadores en este proyecto")
                            proyecto.agregar_empleado_a_proyecto(id_a_modificar)
                        else:
                            proyecto.mostrar_trabajadores_proyecto()
                            print("-. 1 Agrgar trabajador")
                            print("-. 2 eliminar trabajador")
                            print("-. 3 Cancelar")
                            opcion_trabajador = int("Introduce la opcion: ")
                            if opcion_trabajador == 1:
                                proyecto.agregar_empleado_a_proyecto(id_a_modificar)
                            elif opcion_trabajador == 2:
                                proyecto.eliminar_empleado_de_proyecto(id_a_modificar)
                            elif opcion_trabajador == 3:
                                print("Cancelando")
                                break
                    elif opcion == 4:
                        if len(proyecto.tareas) == 0:
                            print("No hay tareas en este proyecto")
                            proyecto.asignar_tarea_a_proyecto(id_a_modificar)
                        else:
                            proyecto.mostrar_tareas_proyecto()
                            print("-. 1 Agrgar Tarea")
                            print("-. 2 eliminar Tarea")
                            print("-. 3 Cancelar")
                            opcion_tarea = int("Introduce la opcion: ")
                            if opcion_tarea == 1:
                                proyecto.asignar_tarea_a_proyecto(id_a_modificar)
                            elif opcion_tarea == 2:
                                proyecto.desasignar_tarea_a_proyecto(id_a_modificar)
                            elif opcion_tarea == 3:
                                print("Cancelando")
                                break
                    elif opcion == 5:
                        print("Cancelando")
                        break
                    else:
                        print("Opción no válida")
      
      
      
    #definimos un metodo para mostrar los trabajadores de un proyecto
    @classmethod
    def mostrar_trabajadores_proyecto(cls, id_proyecto):
        print("Los trabajadores asignados al proyecto son: ")
        for proyecto in cls.lista_proyectos:
            if proyecto.id_proyecto == id_proyecto:
                for worker in proyecto.empleados:
                    worker.mostrar_info_reducida_worker()
     
    #definimos un metodo para mostrar las tareas de un proyecto
    @classmethod
    def mostrar_tareas_proyecto(cls, id_proyecto):
        print("Los trabajadores asignados al proyecto son: ")
        for proyecto in cls.lista_proyectos:
            if proyecto.id_proyecto == id_proyecto:
                for tarea in proyecto.tareas:
                    tarea.mostrar_informacion_basica_tarea()
                    
    #definimos un metodo para mostrar el manager de un proyecto
    @classmethod
    def mostrar_manager_proyecto(cls, id_proyecto):
        for proyecto in cls.lista_proyectos:
            if proyecto.id_proyecto == id_proyecto:
                    proyecto.manager_proyecto.mostrar_info_reducida_manager()
      
    #definimos un metodo para comprobar si el nombre del proyecto ya existe
    @classmethod
    def comprobar_nombre_proyecto(cls, nombre_proyecto):
        for proyecto in cls.lista_proyectos:
            if proyecto.nombre_proyecto == nombre_proyecto:
                return True
            
    #definimos un metodo para comprobar si el proyecto tiene tareas
    @classmethod
    def comprobar_tareas_proyecto(cls,id_proyecto):
        for proyecto in cls.lista_proyectos:
            if proyecto.id_proyecto == id_proyecto:
                if len(proyecto.tareas) == 0:
                    return True
                else:
                    return False