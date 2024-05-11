class Manager_User:
    #definimos el método constructor
    def __init__(self, id_manager : str, nombre_manager : str, apellido_1_manager : str, apellido_2_manager, telefono_manager : int, 
                 email_manager, horas_semanales_manager : float, coste_hora_manager : float, contador_tareas_manager: int, contador_proyectos_manager: int,
                 puesto_trabajo_manager : str)  -> None:
        self.id_manager = id_manager
        self.nombre_manager = nombre_manager
        self.apellido_1_manager = apellido_1_manager
        self.apellido_2_manager = apellido_2_manager
        self.telefono_manager = telefono_manager
        self.email_manager = email_manager
        self.horas_semanales_manager = horas_semanales_manager
        self.coste_hora_manager = coste_hora_manager
        self.contador_tareas_manager = contador_tareas_manager
        self.contador_proyectos_manager = contador_proyectos_manager
        self.puesto_trabajo_manager = puesto_trabajo_manager
    
    #Creamos una lista donde se guardarán los managers
    lista_managers = []

    #definimos un metodo para mostrar la informacción de los managers
    def mostrar_info_ampliada_manager(self):
        print(f"ID: {self.id_manager} \nNombre: {self.nombre_manager} \nPrimer apellido : {self.apellido_1_manager} \nSegundo apellido: {self.apellido_2_manager}") 
        print(f"Telf: {self.telefono_manager} \nEmail: {self.email_manager} \nHoras semanales: {self.horas_semanales_manager} \nCoster hora: {self.coste_hora_manager}") 
        print(f"Tareas asignadas: {self.contador_tareas_manager} \nProyectos asignados:  {self.contador_proyectos_manager}\nPuesto trabajo: {self.puesto_trabajo_manager}")
    
        #definimos un metodo para mostrar la informacción de los managers
    def mostrar_info_reducida_manager(self):
        print(f"ID: {self.id_manager} \n{self.nombre_manager} {self.apellido_1_manager} {self.apellido_2_manager}")
    
    #Definimos un metodo para añadir un nuevo manager
    @classmethod
    def añadir_manager(cls):
        #Creamos un bucle para que el usuario pueda añadir tantos managers como quiera
        while True:
            #Pedimos al usuario que introduzca los datos del manager
            if len(Manager_User.lista_managers) == 0:
                numero_manager=1
                id_manager = "UM" + str(numero_manager)
            else:
                numero_manager = len(Manager_User.lista_managers) + 1
                id_manager = "UM" + str(numero_manager)
            nombre = str(input("Introduce el nombre del manager: "))
            apellido1 = str(input("Introduce el primer apellido: "))
            apellido2 = str(input("Introduce el segundo apellido: "))
            telefono = int(input("Introduce el telefono: "))
            email = str(input("Introduce el email del manager: "))
            horas_semanales = float(input("¿Cuantas horas semanales va a trabajar este manager?: "))
            if horas_semanales > 40:
                print("El manager no puede trabajar más de 40 horas semanales")
            coste_hora = float(input("¿Cuánto ganará el manager a la hora?: "))
            puesto_trabajo = str(input("¿Que puesto de trabajo tendrá el manager?: "))
            #Creamos un objeto de la clase Manager_User
            manager = Manager_User(id_manager, nombre, apellido1, apellido2, telefono, email, horas_semanales, coste_hora, 0, 0, puesto_trabajo)
            #Añadimos el manager a la lista de managers
            Manager_User.lista_managers.append(manager)
            #Pedimos al usuario si quiere añadir otro manager
            añadir_manager = str(input("¿Quieres añadir otro manager? (S/N): "))
            if añadir_manager.upper() == "N":
                break

    #Definimos un metodo para mostrar la lista de managers
    @classmethod
    def mostrar_managers(cls):
        if len(Manager_User.lista_managers) == 0:
            print("No hay ningun usuario manager registrado")
        else:
            #Creamos un bucle para que el usuario pueda ver todos los managers
            for manager in Manager_User.lista_managers:
                manager.mostrar_info_reducida_manager()

    #definimos un metodo para borrar un manager de la lista
    @classmethod
    def borrar_manager(cls):
        if len(Manager_User.lista_managers) == 0:
            print("No hay ningun usuario manager registrado")
        else:
            print("Estos son los managers actualmente")
            #Creamos un bucle para que el usuario pueda ver todos los managers
            Manager_User.mostrar_managers()
            while True:
                id_a_borrar = str(input("Introduce el ID del manager que desea eliminar o cancelar para volver al menu: "))
                if id_a_borrar.lower() != "cancelar":
                    #Creamos un bucle para comprobar el id que deseamos eliminar
                    for manager in Manager_User.lista_managers:
                        if manager.id_manager == id_a_borrar.upper():
                            Manager_User.lista_managers.remove(manager)
                            print("El manager " + str(manager.nombre_manager) + " ha sido eliminado correctamente")
                            break
                        else:
                            print("No existe un manager con el ID introducido")
                            break
                else:
                    print("Volviendo al menu principal")
                    break

    #Definimos un metodo que permita modificar un usuario manager en funcion de su id
    @classmethod
    def modificar_usuario_manager(cls):
        #mostramos los managers que existen actualmente
        if len(Manager_User.lista_managers) == 0:
            print("No hay ningun usuario manager registrado")
        else:
            Manager_User.mostrar_managers()
            id_a_modificar = str(input("Introduce el id del usuario manager que desea modificar: "))
            #Creamos un bucle para comprobar el id que deseamos modificar
            for manager in Manager_User.lista_managers:
                if manager.id_manager == id_a_modificar.upper():
                    print("Estos son los datos del usuario seleccionado")
                    manager.mostrar_info_ampliada_manager()
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
                        print("-. 8 Puesto Trabajo")
                        print("-. 9 Cancelar")
                        dato_a_modificar = int(input("Introduce el numero del dato que desea modificar: "))
                        if dato_a_modificar == 1:
                            nuevo_nombre = str(input("Introduce el nuevo nombre: "))
                            manager.nombre_manager = nuevo_nombre
                            print("El nombre ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 2:
                            nuevo_primer_apellido = str(input("Introduce el nuevo primer apellido: "))
                            manager.apellido_1_manager = nuevo_primer_apellido
                            print("El primer apellido ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 3:
                            nuevo_segundo_apellido = str(input("Introduce el nuevo segundo apellido: "))
                            manager.apellido_2_manager = nuevo_segundo_apellido
                            print("El segundo apellido ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 4:
                            nuevo_telefono = int(input("Introduce el nuevo telefono: "))
                            manager.telefono_manager = nuevo_telefono
                            print("El telefono ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 5:
                            nuevo_email = str(input("Introduce el nuevo email: "))
                            manager.email_manager = nuevo_email
                            print("El email ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 6:
                            nuevas_horas_semanales = float(input("Introduce la cantidad de las nuevas horas que trabajará el manager a la semana: "))
                            if nuevas_horas_semanales > 40:
                                print("El manager no puede trabajar más de 40 horas a la semana")
                                continue
                            manager.horas_semanales_manager = nuevas_horas_semanales
                            print("Las horas semanales han sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 7:
                            nuevo_coste_hora = float(input("¿Cuanto cobrará ahora el manager?: "))
                            manager.coste_hora_manager = nuevo_coste_hora
                            print("El coste hora ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 8:
                            nuevo_puesto_trabajo = float(input("¿Introduce el nuevo puesto de trabajo?: "))
                            manager.puesto_trabajo_manager = nuevo_puesto_trabajo
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
manager1 =  Manager_User("UM1","Antonio", "Sol", "Muñoz", 123456789, "antonio@gmail.com",40 ,8.50,0,0, "Manager de equipo")
Manager_User.lista_managers.append(manager1)