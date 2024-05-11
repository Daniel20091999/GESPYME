
class Administrador_User:
    #Definimos un método constructor
    def __init__(self, id_administrador : str, nombre_administrador : str, apellido_1_administrador : str , apellido_2_administrador : str , telefono_administrador : int,  email_administrador : str,):
        self.id_administrador = id_administrador
        self.nombre_administrador = nombre_administrador
        self.apellido_1_administrador = apellido_1_administrador
        self.apellido_2_administrador = apellido_2_administrador
        self.telefono_administrador = telefono_administrador
        self.email_administrador = email_administrador
    
    #definimos un metodo para mostrar la información reducida de un usuario administrador
    def mostrar_info_reducida_administrador(self):
        print(f"ID: {self.id_administrador} \n{self.nombre_administrador} {self.apellido_1_administrador} {self.apellido_2_administrador}")

    #definimos un metodo para mostrar la información completa de un usuario administrador
    def mostrar_info_completa_administrador(self):
        print(f"ID: {self.id_administrador}\nNombre: {self.nombre_administrador}\nPrimer apellido: {self.apellido_1_administrador}\nSegundo apellido: {self.apellido_2_administrador}")
        print(f"Telefono: {self.telefono_administrador}\nEmail: {self.email_administrador}")
    
    #definimos una lista donde se gurdaran todos los administradores
    lista_administradores = []

    #definimos un metodo para mostrar todos los administradores
    @classmethod
    def mostrar_administradores(cls):
        if len(Administrador_User.lista_administradores) == 0:
            print("No hay ningun usuario administrador registrado")
        else:
            #Creamos un bucle para que el usuario pueda ver todos los administradores
            for administrador in Administrador_User.lista_administradores:
                administrador.mostrar_info_reducida_administrador()
    
    #definimos un metodo para borrar un administrador de la lista
    @classmethod
    def borrar_administrador(cls):
        if len(Administrador_User.lista_administradores) == 0:
            print("No hay ningun usuario administrador registrado")
        else:
            print("Estos son los administradores actualmente")
            #Creamos un bucle para que el usuario pueda ver todos los administradores
            Administrador_User.mostrar_administradores()
            id_a_borrar = str(input("Introduce el ID del administrador que desea eliminar: "))
            #Creamos un bucle para comprobar el id que deseamos eliminar
            for administrador in Administrador_User.lista_administradores:
                if administrador.id_administrador == id_a_borrar.upper():
                    Administrador_User.lista_administradores.remove(administrador)
                    print("El administrador " + str(administrador.nombre_administrador) + " ha sido eliminado correctamente")
                    break
                else:
                    print("No existe un administrador con el ID introducido")
                    break

    #Definimos un metodo para añadir un nuevo administrador
    @classmethod
    def añadir_administrador(cls):
        #Creamos un bucle para que el usuario pueda añadir tantos administradores como quiera
        while True:
            #Pedimos al usuario que introduzca los datos del manager
            if len(Administrador_User.lista_administradores) == 0:
                numero_administrador=1
                id_administrador = "UA" + str(numero_administrador)
            else:
                numero_administrador = len(Administrador_User.lista_administradores) + 1
                id_administrador = "UA" + str(numero_administrador)
            nombre = str(input("Introduce el nombre del administrador: "))
            apellido1 = str(input("Introduce el primer apellido: "))
            apellido2 = str(input("Introduce el segundo apellido: "))
            telefono = int(input("Introduce el telefono: "))
            email = str(input("Introduce el email del administrador: "))
            #Creamos un objeto de la clase Administrador_User
            administrador = Administrador_User(id_administrador, nombre, apellido1, apellido2, telefono, email)
            #Añadimos el manager a la lista de administradores
            Administrador_User.lista_administradores.append(administrador)
            #Pedimos al usuario si quiere añadir otro administrador
            añadir_administrador = str(input("¿Quieres añadir otro administrador? (S/N): "))
            if añadir_administrador.upper() == "N":
                break

    #Definimos un metodo que permita modificar un usuario administrador en funcion de su id
    @classmethod
    def modificar_usuario_administrador(cls):
        #mostramos los administradores que existen actualmente
        if len(Administrador_User.lista_administradores) == 0:
            print("No hay ningun usuario administrador registrado")
        else:
            Administrador_User.mostrar_administradores()
            id_a_modificar = str(input("Introduce el id del usuario administrador que desea modificar: "))
            #Creamos un bucle para comprobar el id que deseamos modificar
            for administrador in Administrador_User.lista_administradores:
                if administrador.id_administrador == id_a_modificar.upper():
                    print("Estos son los datos del usuario seleccionado")
                    administrador.mostrar_info_completa_administrador()
                    #Creamos un bucle para que el usuario pueda modificar los datos
                    while True:
                        print("¿Que dato desea modificar?")
                        print("-. 1 Nombre")
                        print("-. 2 Primer apellido")
                        print("-. 3 Segundo apellido")
                        print("-. 4 Telefono")
                        print("-. 5 Email")
                        print("-. 6 Cancelar")
                        dato_a_modificar = int(input("Introduce el numero del dato que desea modificar: "))
                        if dato_a_modificar == 1:
                            nuevo_nombre = str(input("Introduce el nuevo nombre: "))
                            administrador.nombre_administrador = nuevo_nombre
                            print("El nombre ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 2:
                            nuevo_primer_apellido = str(input("Introduce el nuevo primer apellido: "))
                            administrador.apellido_1_administrador = nuevo_primer_apellido
                            print("El primer apellido ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 3:
                            nuevo_segundo_apellido = str(input("Introduce el nuevo segundo apellido: "))
                            administrador.apellido_2_administrador = nuevo_segundo_apellido
                            print("El segundo apellido ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 4:
                            nuevo_telefono = int(input("Introduce el nuevo telefono: "))
                            administrador.telefono_administrador = nuevo_telefono
                            print("El telefono ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 5:
                            nuevo_email = str(input("Introduce el nuevo email: "))
                            administrador.email_administrador = nuevo_email
                            print("El email ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 6:
                            print("Cancelando")
                            break
                        else:
                            print("Opción no válida")
                            
#definimos un administrador nuevo y lo añadimos a la lista
administrador1 =  Administrador_User("UA1","Daniel", "Garcia", "Muñoz", 123456789, "daniel@gmail.com")
Administrador_User.lista_administradores.append(administrador1)