
class Worker_User:
    #definimos el método constructor
    def __init__(self, id_worker : str, nombre_worker : str, apellido_1_worker : str, apellido_2_worker : str, telefono_worker : int, 
                 email_worker, horas_semanales_worker : float, coste_hora_worker : float, contador_tareas_worker: int, puesto_trabajo_worker: str,
                 contador_proyectos_worker : int)  -> None:
        self.id_worker = id_worker
        self.nombre_worker = nombre_worker
        self.apellido_1_worker = apellido_1_worker
        self.apellido_2_worker = apellido_2_worker
        self.telefono_worker = telefono_worker
        self.email_worker = email_worker
        self.horas_semanales_worker = horas_semanales_worker
        self.coste_hora_worker = coste_hora_worker
        self.contador_tareas_worker = contador_tareas_worker
        self.puesto_trabajo_worker = puesto_trabajo_worker
        self.contador_proyectos_worker = contador_proyectos_worker

    #Creamos una lista donde se guardarán los workers
    lista_workers = []

    #definimos un metodo para mostrar la informacción de los managers
    
    def mostrar_info_ampliada_workers(self):
        print(f"ID: {self.id_worker} \nNombre: {self.nombre_worker} \nPrimer apellido : {self.apellido_1_worker} \nSegundo apellido: {self.apellido_2_worker}") 
        print(f"Telf: {self.telefono_worker} \nEmail: {self.email_worker} \nHoras semanales: {self.horas_semanales_worker} \nCoster hora: {self.coste_hora_worker}") 
        print(f"Tareas asignadas: {self.contador_tareas_worker} \nPuesto trabajo:  {self.puesto_trabajo_worker}\nNº Proyectos: {self.contador_proyectos_worker}")
    
    #definimos un metodo para mostrar la informacción de los managers
    
    def mostrar_info_reducida_worker(self):
        print(f"ID: {self.id_worker} \n{self.nombre_worker} {self.apellido_1_worker} {self.apellido_2_worker}")
    
    #Definimos un metodo para añadir un nuevo manager
    @classmethod
    def añadir_worker(cls):
        #Creamos un bucle para que el usuario pueda añadir tantos managers como quiera
        while True:
            #Pedimos al usuario que introduzca los datos del manager
            if len(Worker_User.lista_workers) == 0:
                numero_worker=1
                id_worker = "UW" + str(numero_worker)
            else:
                numero_worker = len(Worker_User.lista_workers) + 1
                id_worker = "UW" + str(numero_worker)
            nombre = str(input("Introduce el nombre del trabajador: "))
            apellido1 = str(input("Introduce el primer apellido: "))
            apellido2 = str(input("Introduce el segundo apellido: "))
            telefono = int(input("Introduce el telefono: "))
            email = str(input("Introduce el email del trabajador: "))
            horas_semanales = float(input("¿Cuantas horas semanales va a trabajar este trabajador?: "))
            if horas_semanales > 40:
                print("El trabajador no puede trabajar más de 40 horas semanales")
            coste_hora = float(input("¿Cuánto ganará el trabajador a la hora?: "))
            puesto_trabajo = str(input("¿En que puesto trabajará el trabajador?"))
            #Creamos un objeto de la clase Worker_User
            worker = Worker_User(id_worker, nombre, apellido1, apellido2, telefono, email, horas_semanales, coste_hora, 0, puesto_trabajo,0)
            #Añadimos el worker a la lista de workers
            Worker_User.lista_workers.append(worker)
            #Pedimos al usuario si quiere añadir otro worker
            añadir_worker = str(input("¿Quieres añadir otro trabajador? (S/N): "))
            if añadir_worker.upper() == "N":
                break

    #Definimos un metodo para mostrar la lista de trabajadores
    @classmethod
    def mostrar_workers(cls):
        if len(Worker_User.lista_workers) == 0:
            print("No hay ningun usuario worker registrado")
        else:
            #Creamos un bucle para que el usuario pueda ver todos los trabajadores
            for worker in cls.lista_workers:
                worker.mostrar_info_reducida_worker()

    #definimos un metodo para borrar un trabajador de la lista
    @classmethod
    def borrar_worker(cls):
        if len(Worker_User.lista_workers) == 0:
            print("No hay ningun usuario worker registrado")
        else:
            print("Estos son los trabajadores actualmente")
            #Creamos un bucle para que el usuario pueda ver todos los managers
            Worker_User.mostrar_info_reducida_worker()
            id_a_borrar = str(input("Introduce el ID del manager que desea eliminar: "))
            #Creamos un bucle para comprobar el id que deseamos eliminar
            for worker in Worker_User.lista_workers:
                if worker.id_worker == id_a_borrar.upper():
                    Worker_User.lista_workers.remove(worker)
                    print("El trabajador " + str(worker.nombre_worker) + " ha sido eliminado correctamente")
                    break
                else:
                    print("No existe un trabajador con el ID introducido")
                    break

    #Definimos un metodo que permita modificar un usuario manager en funcion de su id
    @classmethod
    def modificar_usuario_worker(cls):
        #mostramos los managers que existen actualmente
        if len(cls.lista_workers) == 0:
            print("No hay ningun usuario worker registrado")
        else:
            Worker_User.mostrar_workers()
            id_a_modificar = str(input("Introduce el id del usuario worker que desea modificar: "))
            #Creamos un bucle para comprobar el id que deseamos modificar
            for worker in cls.lista_workers:
                if worker.id_worker == id_a_modificar.upper():
                    print("Estos son los datos del usuario seleccionado")
                    worker.mostrar_info_ampliada_workers()
                    #Creamos un bucle para que el usuario pueda modificar los datos
                    while True:
                        print("¿Que dato desea modificar?")
                        print("-. 1 Nombre")
                        print("-. 2 Primer apellido")
                        print("-. 3 Segundo apellido")
                        print("-. 4 Telefono")
                        print("-. 5 Email")
                        print("-. 6 Horas semanales")
                        print("-. 7 Coste hora")
                        print("-. 8 Puesto trabajo")
                        print("-. 9 Cancelar")
                        dato_a_modificar = int(input("Introduce el numero del dato que desea modificar: "))
                        if dato_a_modificar == 1:
                            nuevo_nombre = str(input("Introduce el nuevo nombre: "))
                            worker.nombre_worker = nuevo_nombre
                            print("El nombre ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 2:
                            nuevo_primer_apellido = str(input("Introduce el nuevo primer apellido: "))
                            worker.apellido_1_worker = nuevo_primer_apellido
                            print("El primer apellido ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 3:
                            nuevo_segundo_apellido = str(input("Introduce el nuevo segundo apellido: "))
                            worker.apellido_2_worker = nuevo_segundo_apellido
                            print("El segundo apellido ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 4:
                            nuevo_telefono = int(input("Introduce el nuevo telefono: "))
                            worker.telefono_worker = nuevo_telefono
                            print("El telefono ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 5:
                            nuevo_email = str(input("Introduce el nuevo email: "))
                            worker.email_worker = nuevo_email
                            print("El email ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 6:
                            nuevas_horas_semanales = float(input("Introduce la cantidad de las nuevas horas que trabajará el trabajador a la semana: "))
                            if nuevas_horas_semanales > 40:
                                print("Las horas semanales no pueden ser mayores a 40")
                                continue
                            worker.horas_semanales_worker = nuevas_horas_semanales
                            print("Las horas semanales han sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 7:
                            nuevo_coste_hora = float(input("¿Cuanto cobrará ahora el trabajador? : "))
                            worker.coste_hora_worker = nuevo_coste_hora
                            print("El coste ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 8:
                            nuevo_puesto_trabajo = float(input("¿Cual es el nuevo puesto de trabajo del trabajador? : "))
                            worker.puesto_trabaajo_worker= nuevo_puesto_trabajo
                            print("El puesto de trabajo ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 9:
                            print("Cancelando")
                            break


#definimos un manager nuevo y lo añadimos a la lista
worker1 =  Worker_User("UW1","Jose", "Garcia", "Perez", 123456789, "jose@gmail.com",40 ,8.50,0,"Programador",0)
Worker_User.lista_workers.append(worker1)