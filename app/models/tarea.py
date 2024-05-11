from datetime import datetime as dt
from worker_user import Worker_User
from manager_user import Manager_User
class Tarea:
    #definimos un metodo constructor
    def __init__(self, id_tarea : str, nombre_tarea : str, tiempo_estimado : int, fecha_inicio : dt, fecha_fin : dt,
                 fecha_limite : dt, coste_tarea : float, estado_tarea: bool ,id_proyecto: str, trabajadores: list):
        self.id_tarea = id_tarea
        self.nombre_tarea = nombre_tarea
        self.tiempo_estimado = tiempo_estimado
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_limite = fecha_limite
        self.coste_tarea = coste_tarea
        self.estado_tarea = estado_tarea
        self.id_proyecto = id_proyecto
        self.trabajadores = trabajadores
    
    #definimos una lista donde guardaremos las tareas
    lista_tareas = []
    #definimos un metodo para mostrar la información básica de una tarea
    def mostrar_informacion_basica_tarea(self):
        print(f"ID : {self.id_tarea}\n Nombre {self.nombre_tarea}\nFecha inicio: {self.fecha_inicio}\nFecha fin: {self.fecha_fin}")
    
    #definimos un metodo para mostrar la información completa de una tarea
    def mostrar_informacion_completa_tarea(self):
        print(f"ID : {self.id_tarea}\n Nombre {self.nombre_tarea}\nTiempo estimado en días: {self.tiempo_estimado}\nFecha inicio: {self.fecha_inicio}\nFecha fin: {self.fecha_fin}")
        print(f"Fecha límite {self.fecha_limite}\nCoste: {self.coste_tarea}\nEstado: {self.estado_tarea}\nProyecto: {self.id_proyecto}")
        Tarea.mostrar_trabajadores_tarea(self.id_tarea)
        
    
    #definimos un metodo para añadir una tarea a la lista de tareas
    @classmethod
    def añadir_tarea(cls):
        if len(cls.lista_tareas) == 0:
            numero_tarea = 1
            id_tarea = "T" + str(numero_tarea)
        else:
            numero_tarea = len(cls.lista_tareas) +1
            id_tarea = "T" + str(numero_tarea)
        nombre_tarea = str(input("Introduce el nombre de la tarea: "))
        tiempo_estimado = dt.strptime(input("Introduce los días estimados que se tardarán en realizar la tarea: "),'%d')
        fecha_inicio = dt.strptime(input("Introduce la fecha de inicio de la tarea (dia/mes/año): "), '%d/%m/%y')
        fecha_fin = dt.strptime(input("Introduce la fecha de fin de la tarea (dia/mes/año): "), '%d/%m/%y')
        fecha_limite = dt.strptime(input("Introduce la fecha límite para poder realizar la tarea(dia/mes/año): "), '%d/%m/%y')
        coste_tarea = 0
        estado_tarea = False
        proyecto = ""
        trabajadores = []
        #creamos una tarea con los datos obtenidos y la añadimos a la lista de tareas
        nueva_tarea = Tarea(id_tarea, nombre_tarea, tiempo_estimado, fecha_inicio, fecha_fin, fecha_limite, coste_tarea,estado_tarea,proyecto,trabajadores)
        cls.lista_tareas.append(nueva_tarea)
        print("Tarea creada correctamente")
    
    #definimos un método para mostrar todas las tareas
    @classmethod
    def mostrar_tareas(cls):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            for tareas in cls.lista_tareas:
                tareas.mostrar_informacion_basica_tarea() 
    
    #definimos un metodo para eliminar una tarea de la lista de tareas
    @classmethod
    def eliminar_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("No hay tareas para eliminar")
        else:
            id_a_eliminar = str(input("Por favor introduce el ID de la tarea que desea eliminar o cancelar para volver al menu: "))
            if id_a_eliminar.lower() != "cancelar":
                for tareas in cls.lista_tareas:
                    if tareas.id_tarea == id_a_eliminar:
                        cls.lista_tareas.remove(tareas)
                        print("Tarea eliminada correctamente")
                    else:
                        print("No existe ninguna tarea con ese ID")
            else:
                print("Volviendo al menu")
                        
    #definimos un método para asignar un trabajador a la tarea
    @classmethod
    def asignar_trabajador_a_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            Tarea.mostrar_tareas()
            id_tarea = str(input("Introduce el id de la tarea a la que se le quiere añadir trabajadores: "))
            for tarea in cls.lista_tareas:
                if tarea.id_tarea == id_tarea:
                    if len(Worker_User.lista_workers) == 0:
                        print("No existen trabajadores todavia")
                    else:
                        while True:
                            print("Estos son los trabajadores existentes actualmente")
                            Worker_User.mostrar_workers()
                            id_trabajador = str(input("Introduce el id del trabajador que quieres añadir a la tarea o cancelar para volver al menu: "))
                            for trabajador in Worker_User.lista_workers:
                                if trabajador.id_worker == id_trabajador:
                                    tarea.trabajadores.append(trabajador)
                                    #aumentamos el contador de tareas del trabajador en 1
                                    trabajador.contador_tareas_worker += 1
                                    print("Trabajador añadido correctamente")
                                    opcion = str(input("¿Quieres añadir otro trabajador? (S/N): "))
                                    if opcion == "S":
                                        continue
                                    else:
                                        break
                                elif id_trabajador.lower() == "cancelar":
                                    print("Volviendo al menu")
                                    break
                                else:
                                    print("No existe ese trabajador")
                            break

                                    
    #definimos un metodo para eliminar un trabajador ya sea manager o worker de una tarea
    @classmethod
    def eliminar_trabajador_de_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            cls.mostrar_tareas()
            id_tarea = str(input("Introduce el id de la tarea de la que quieres eliminar un trabajador ocancelar para volver: "))
            if id_tarea.lower() != "cancelar":                
                for tarea in cls.lista_tareas:
                    if tarea.id_tarea == id_tarea:
                        for worker in tarea.trabajadores:
                            worker.mostrar_info_reducida_worker()
                            id_trabajador_a_eliminar = str(input("introduce el id del trabajador que desea eliminar: "))
                            for trabajador in tarea.trabajadores:
                                trabajador.id_worker = id_trabajador_a_eliminar
                                #reducimos el contador de tareas del trabajador en 1
                                trabajador.contador_tareas_worker -= 1
                                #eliminamos el trabajador de la lista de trabajadores de la tarea
                                tarea.trabajadores.remove(trabajador)
                                print("Trabajador eliminado correctamente")
                                break
                            break
                    else:
                        print("No existe una tarea con ese ID")
            else:
                print("Volviendo al menú")
                           
    #definimos un método para modificar el estado de una tarea
    @classmethod
    def finalizar_tarea(cls, id_tarea):
        if len(cls.lista_tareas) == 0:
            print("No existen tareas todavia")
        else:
            cls.mostrar_tareas()
            for tarea in cls.lista_tareas:
                if tarea.id_tarea == id_tarea:
                        tarea.estado = True
                        #actualizamos la fecha fin por la de ahora
                        tarea.fecha_fin = dt.now()
                        #al finalizar la tarea calculamos el coste de la tarea
                        cls.calculo_coste_tarea(id_tarea)
                        print("Tarea finalizada correctamente")

    #definimos un método para calcular el coste de una tarea
    @classmethod
    def calculo_coste_tarea(cls, id_tarea):
        for tarea in cls.lista_tareas:
            if tarea.id_tarea == id_tarea:
                #comprobamos que la tarea se haya finalizado
               if tarea.estado == True:
                   #calculamos el tiempo real tardado
                   tiempo_final = dt.strptime((tarea.fecha_fin - tarea.fecha_inicio),'%d')
                   #calculamos el coste hora de cada uno de los trabajadores asignados a la tarea
                   for trabajador in tarea.trabajadores:
                       coste_hora_trabajadores = sum(trabajador.coste_hora) * float(tiempo_final)
                       #asignamos el valor calculado al coste de la tarea
                       tarea.coste_tarea = coste_hora_trabajadores
                       print("El coste de la tarea es: ", tarea.coste_tarea)
               else:
                   print("La tarea no se ha finalizado")
    
    #definimos un método para mostrar las tareas de un trabajador
    @classmethod
    def mostrar_tareas_trabajador(cls, id_trabajador):
        print("Tus tareas son las siguientes")
        for trabajador in Worker_User.lista_workers:
            if trabajador.id_worker == id_trabajador:
                for tarea in cls.lista_tareas:
                    if tarea.trabajadores == trabajador.id_worker:
                        tarea.mostrar_informacion_basica_tarea()
            else:
                print("No tienes tareas asignadas")

    #definimos un metodo para mostrar los trabajadores de una tarea
    @classmethod
    def mostrar_trabajadores_tarea(cls, id_tarea):
        print("Los trabajadores asignados a la tarea son: ")
        for tarea in cls.lista_tareas:
            if tarea.id_tarea == id_tarea:
                for worker in tarea.trabajadores:
                    worker.mostrar_info_reducida_worker()
            
    #definimos un método para modificar los datos de una tarea
    @classmethod
    def modificar_datos_tarea(cls):
        if len(cls.lista_tareas) == 0:
            print("Aún no existen tareas")
        else:
            cls.mostrar_tareas()
            id_a_modificar = str(input("Introduce el ID de la tarea a modificar"))
            for tarea in cls.lista_tareas:
                if tarea.id_tarea == id_a_modificar:
                    print("Estos son los datos de la tarea seleccionada")
                    tarea.mostrar_informacion_completa_tarea()
                    #creamos un bucle para que el usuario pueda modificar los datos de la tarea
                    while True:
                        print("¿Que dato desea modificar?")
                        print("-. 1 Nombre Tarea")
                        print("-. 2 Tiempo estimado")
                        print("-. 3 Fecha inicio")
                        print("-. 4 Fecha fin")
                        print("-. 5 Fecha liminite")
                        print("-. 6 Coste tarea")
                        print("-. 7 Estado tarea")
                        print("-. 8 Cancelar")
                        dato_a_modificar = int(input("Introduce el numero del dato que desea modificar: "))
                        if dato_a_modificar == 1:
                            nuevo_nombre = str(input("Introduce el nuevo nombre de la tarea: "))
                            tarea.nombre_tarea = nuevo_nombre
                            print("Nombre modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 2:
                            nuevo_tiempo_estimado = int(input("Introduce el nuevo tiempo estimado de la tarea en dias: "))
                            tarea.tiempo_estimado = nuevo_tiempo_estimado
                            print("Tiempo estimado modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 3:
                            nueva_fecha_inicio = dt.strptime(input("Introduce la nueva fecha de inicio en dd/mm/y:" ),'%d/%m/%y')
                            tarea.fecha_inicio = nueva_fecha_inicio
                            print("fecha inicio modificada correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 4:
                            nueva_fecha_fin = dt.strptime(input("Introduce la nueva fecha de fin en dd/mm/y:" ),'%d/%m/%y')
                            tarea.fecha_fin = nueva_fecha_fin
                            print("fecha fin modificada correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 5:
                            nueva_fecha_limite = dt.strptime(input("Introduce la nueva fecha limite: "), '%d/%%m/%y')
                            tarea.fecha_limite = nueva_fecha_limite
                            print("fecha limite modificada correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 6:
                            nuevo_coste_tarea = float(input("introduce el nuevo coste de la tarea: "))
                            tarea.coste_tarea = nuevo_coste_tarea
                            print("Coste tarea modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 7:
                            nuevo_estado_tarea = str(input("Se ha finalizado la tarea? (S/N): "))
                            if nuevo_estado_tarea.upper() == "S":
                                Tarea.finalizar_tarea(id_a_modificar)
                            else:
                                tarea.estado = False
                            print("Estado modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 8:
                            print("Cancelando")
                            break
                        else:
                            print("opcion no valida")
                else:
                    print("No existe ninguna tarea con ese ID")