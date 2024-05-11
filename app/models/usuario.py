import os
from administrador_user import Administrador_User
from worker_user import Worker_User
from manager_user import Manager_User
from proyecto import Proyecto
from tarea import Tarea
class Usuario:
    #Definimos el metodo constructor
    def __init__(self, id_usuario : int, nombre_usuario : str, contrasena_usuario : str, tipo_usuario: str, id_empleado: str ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena_usuario = contrasena_usuario
        self.tipo_usuario = tipo_usuario
        self.id_empleado = id_empleado

    #Definimos una lista vacia donde se guradarán los datos de los usuarios
    lista_usuarios = []

    #Definimos el metodo para mostrar la informacion de cada usuario
    def mostrar_datos_usuario(self):
        print(f"ID: {self.id_usuario} \nUsuario: {self.nombre_usuario}\nContraseña: {self.contrasena_usuario}\nTipo Usuario: {self.tipo_usuario}")

    #Definimos el metodo para agregar un usuario a la lista
    @classmethod
    def agregar_usuario(cls):
        if len(Usuario.lista_usuarios) == 0:
            numero_usuario = 1
            id_usuario = "U" + str(numero_usuario)
        else:
            numero_usuario = len(Usuario.lista_usuarios) +1
            id_usuario = "U" + str(numero_usuario)
            nombre = str(input("Introduce el nombre del usuario: "))
            if cls.comprobar_nombre_usuario(nombre) == True:
                print("El nombre de usuario ya existe")
            else: 
                contrasena = str(input("Introduce la contraseña del usuario: "))
                confirmar_contrasena = str(input("Confirma la contraseña: "))
                if contrasena != confirmar_contrasena:
                    print("Las contraseñas no coinciden")
                else:
                    tipo_usuario = str(input("Introduce el tipo de usuario pueden ser administrador | worker | manager: "))
                    if tipo_usuario.lower() != "administrador" and tipo_usuario.lower() != "worker" and tipo_usuario.lower() != "manager":
                        print("Tipo de usuario incorrecto")
                    elif tipo_usuario.lower() == "administrador":
                        #Creamos un objeto de la clase Usuario con los datos introducidos por el usuario
                        id_empleado = id_usuario
                    else:
                        id_empleado =""
                    usuario = Usuario(id_usuario, nombre, contrasena, tipo_usuario,id_empleado)
                    #Agregamos el objeto a la lista de usuarios
                    Usuario.lista_usuarios.append(usuario)
                    print("Usuario agregado correctamente")
        
    #definimos un metodo para mostrar los usuarios
    @classmethod
    def mostrar_usuarios(cls):
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado")
        else:
            #Creamos un bucle para que el usuario pueda ver todos los usuarios creados
            for usuario in Usuario.lista_usuarios:
                usuario.mostrar_datos_usuario()
    
    #definimos un metodo para eliminar un usuario en funcion de su id
    @classmethod
    def eliminar_usuario(cls):
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado")
        else:
            print("Estos son los usuarios actualmente")
            #Creamos un bucle para que el usuario pueda ver todos los usuarios creados
            Usuario.mostrar_usuarios()
            id_a_borrar = str(input("Introduce el ID del usuario que desea eliminar: "))
            #Creamos un bucle para comprobar el id que deseamos eliminar
            for user in Usuario.lista_usuarios:
                if user.id_usuario == id_a_borrar.upper():
                    Usuario.lista_usuarios.remove(user)
                    print("El usuario " + str(user.nombre_usuario) + " ha sido eliminado correctamente")
                    break
                else:
                    print("No existe un usuario con el ID introducido")
                    break
    
    #Definimos un metodo que permita modificar un usuario en funcion de su id
    @classmethod
    def modificar_usuario(cls):
        #mostramos los managers que existen actualmente
        if len(Usuario.lista_usuarios) == 0:
            print("No hay ningun usuario registrado")
        else:
            Usuario.mostrar_usuarios()
            id_a_modificar = str(input("Introduce el id del usuario manager que desea modificar: "))
            #Creamos un bucle para comprobar el id que deseamos modificar
            for user in Usuario.lista_usuarios:
                if user.id_usuario == id_a_modificar.upper():
                    print("Estos son los datos del usuario seleccionado")
                    user.mostrar_datos_usuario()
                    #Creamos un bucle para que el usuario pueda modificar los datos
                    while True:
                        print("¿Que dato desea modificar?")
                        print("-. 1  usuario")
                        print("-. 2 contraseña")
                        print("-. 3 Cancelar")
                        dato_a_modificar = int(input("Introduce el numero del dato que desea modificar: "))
                        if dato_a_modificar == 1:
                            nuevo_nombre = str(input("Introduce el nuevo nombre de usuario: "))
                            user.nombre_usuario = nuevo_nombre
                            print("El nombre de usuario ha sido modificado correctamente")
                            opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                            if opcion.upper() == "S":
                                continue
                            elif opcion.upper() == "N":
                                break
                        elif dato_a_modificar == 2:
                            nueva_contrasena = str(input("Introduce la nueva contraseña: "))
                            confirmar_contrasena = str(input("Confirma la contraseña: "))
                            if nueva_contrasena != confirmar_contrasena:
                                print("Las contraseñas no coinciden")
                            else:
                                user.contrasena = nueva_contrasena
                                print("La contrasena ha sido modificado correctamente")
                                opcion = str(input("Desea modificar algun otro dato? (S/N)"))
                                if opcion.upper() == "S":
                                    continue
                                elif opcion.upper() == "N":
                                    break
                        elif dato_a_modificar == 3:
                            print("Cancelando")
                            break
    
    #Definimos un metodo para que el usuario inicie sesión
    @classmethod
    def iniciar_sesion(cls):
        usuario_inicio_sesion = str(input("Introduce el nombre de usuario: "))
        #comprobamos que el usuario existe en la lista de usuarios
        for usuario in Usuario.lista_usuarios:
            if usuario.nombre_usuario == usuario_inicio_sesion:
                contrasena_inicio_sesion = str(input("Introduce la contraseña: "))
                if usuario.contrasena_usuario == contrasena_inicio_sesion:
                    print("Sesión iniciada correctamente")
                    if usuario.tipo_usuario == "administrador":
                        Menu.menu_final_administrador()
                        return usuario
                    elif usuario.tipo_usuario == "worker":
                        Menu.menu_final_worker()
                        break
                    elif usuario.tipo_usuario == "manager":
                        Menu.menu_final_manager()
                        break
                else:
                    print("La contraseña es incorrecta")
            else:
                print("El usuario no existe")
     

    #definimos una funcion para asigar un worker user a un usuario
    @classmethod
    def asignar_worker_usuario(cls):
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == "" and usuario.tipo_usuario == "worker":
                print("Estos son los usuarios de tipo worker que no tienen un worker asignado asignado")
                usuario.mostrar_datos_usuarios()
                print("Estos son los workers existentes actualmente")
                Worker_User.mostrar_workers()
                id_empleado_seleccionado = str(input("Por favor escribe el ID del administrador que tendrá asignado a este usuario: "))
                if Usuario.comprobar_id_empleado(id_empleado_seleccionado == False):
                    print("Ese usuario ya a sido asignado a un worker, por favor seleccione otro ID")
                else: 
                    usuario.id_empleado = id_empleado_seleccionado
                    print("El usuario ha sido asignado correctamente")
            else:
                print("No hay usuarios de tipo worker que no tengan un worker asignado")
        
    #definimos una funcion para asigar un worker user a un usuario
    @classmethod
    def asignar_manager_usuario(cls):
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == "" and usuario.tipo_usuario == "manager":
                print("Estos son los usuarios de tipo manager que no tienen un manager asignado asignado")
                usuario.mostrar_datos_usuario()
                print("Estos son los managers existentes actualmente")
                Manager_User.mostrar_managers()
                id_empleado_seleccionado = str(input("Por favor escribe el ID del manager que tendrá asignado a este usuario: "))
                if Usuario.comprobar_id_empleado(id_empleado_seleccionado):
                    print("Ese usuario ya a sido asignado a un manager, por favor seleccione otro ID")
                else: 
                    usuario.id_empleado = id_empleado_seleccionado
                    print("El usuario ha sido asignado correctamente")
            else:
                print("No hay usuarios de tipo manager que no tengan un manager asignado")
    
    #definimos una funcion para asigar un administrador user a un usuario
    @classmethod
    def asignar_admin_usuario(cls):
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == "" and usuario.tipo_usuario == "administrador":
                print("Estos son los usuarios de tipo administrador que no tienen un administrador asignado asignado")
                usuario.mostrar_datos_usuarios()
                print("Estos son los administradores existentes actualmente")
                Administrador_User.mostrar_administradores()
                id_empleado_seleccionado = str(input("Por favor escribe el ID del administrador que tendrá asignado a este usuario: "))
                if Usuario.comprobar_id_empleado(id_empleado_seleccionado == False):
                    print("Ese usuario ya a sido asignado a un administrador, por favor seleccione otro ID")
                else: 
                    usuario.id_empleado = id_empleado_seleccionado
                    print("El usuario ha sido asignado correctamente")
            else:
                print("No hay usuarios de tipo administrador que no tengan un administrador asignado")

    #definimos un metodo para saber si el id_empleado ya está en uso
    @classmethod
    def comprobar_id_empleado(cls, id_empleado):
        for usuario in Usuario.lista_usuarios:
            if usuario.id_empleado == id_empleado:
                return True
            
            
    
    #definimos un método para comprobar si el nombre de usuario ya existe en la lista de usuarios
    @classmethod
    def comprobar_nombre_usuario(cls, nombre_usuario):
        for usuario in Usuario.lista_usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return False
    
    #definimos un método para que el usuario pueda recuperar su contraseña
    @classmethod
    def recuperar_contraseña(cls):
        email_usuario = str(input("Por favor introduce el email para mandarle las instrucciones para recuperar su contraseña: "))
        if cls.comprobar_email_admin(email_usuario) == False and cls.comprobar_email_manager(email_usuario) == False and cls.comprobar_email_worker(email_usuario) == False:
            print("No exixte ningun usuario con ese email, por favor pruebe con otra cuenta")
    
    #Definimos una funcion que limpie la pantalla
    @classmethod
    def limpiar_pantalla(cls):
        os.system('cls' if os.name=='nt' else 'clear')
        
    #creamos un metodo para comprobar si hay algún worker con el email introducido
    @classmethod
    def comprobar_email_worker(cls, email):
        for administrador in Administrador_User.lista_administradores:
            if administrador.email_administrador == email:
                print("Se ha enviado un email a la dirección indicada con las instrucciones para recuperar su contraseña")
                return True
            else:
                return False  

    #creamos un metodo para comprobar si hay algún admin con el email introducido
    @classmethod
    def comprobar_email_admin(cls, email):
        for administrador in Administrador_User.lista_administradores:
            if administrador.email_administrador == email:
                print("Se ha enviado un email a la dirección indicada con las instrucciones para recuperar su contraseña")
                return True
            else:
                return False  

    #creamos un metodo para comprobar si hay algún manager con el email introducido
    @classmethod
    def comprobar_email_manager(cls, email):
        for manager in Manager_User.lista_managers:
            if manager.email_manager == email:
                print("Se ha enviado un email a la dirección indicada con las instrucciones para recuperar su contraseña")
                return True
            else:
                return False


class Menu:

        
    #definimos el menu inicial de usuarios
    @classmethod
    def menu_principal(cls):
        while True:
            print("Hola, Bienvenido a GESPYME")
            print("-. 1 Iniciar sesión")
            print("-. 2 recuperar contraseña")
            print("-. 3 Salir")
            opcion = int(input("Elije que quieres hacer: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                Usuario.iniciar_sesion()
            elif opcion == 2:
                cls.limpiar_pantalla()
                Usuario.recuperar_contraseña()
            elif opcion == 3:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
                
    
    #definimos el menú final de los administradores
    @classmethod
    def menu_final_administrador(cls):
        while True:
            print("-. 1 Gestionar Managers")
            print("-. 2 Gestiones Administrador")
            print("-. 3 Acceder a funcionalidades de Manager")
            print("-. 4 Salir")
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                cls.menu_gestion_managers()
            elif opcion == 2:
                cls.limpiar_pantalla()
                cls.menu_gestiones_administrador()
            elif opcion == 3:
                cls.limpiar_pantalla()
                Menu.menu_final_manager()
            elif opcion == 4:
                cls.limpiar_pantalla()
                print("Cerrando sesión")
                cls.menu_principal()
                break
    
    #definimos el menú final del usuario manager
    @classmethod
    def menu_final_manager(cls):
        while True:
            print("-. 1 Gestionar trabajadores")
            print("-. 2 Gestionar Proyectos")
            print("-. 3 Gestionar Tareas")
            print(".- 4 Salir")
            opcion = int(input("Por favor introduce una opción: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                Menu.menu_gestion_workers()
            elif opcion == 2:
                cls.limpiar_pantalla()
                cls.menu_gestion_proyectos()
            elif opcion == 3:
                cls.limpiar_pantalla()
                cls.menu_gestion_tareas()
            elif opcion == 4:
                cls.limpiar_pantalla()
                print("Cerrando sesión")
                cls.menu_principal()
                break                   

    #Definimos el menú final de un worker
    @classmethod
    def menu_final_worker(cls):
        while True:
            print("-.1 Mostrar tareas asignadas")
            print("-. 2 Salir")
            opcion = int(input("Elije que quieres hacer: "))
            if opcion == 1:
                cls.limpiar_pantalla()
                Tarea.mostrar_tareas_trabajador()
            elif opcion == 2:
                cls.limpiar_pantalla()
                print("Hasta luego")
                break
    
    #definimos un menu para la gestion de trabajadores de los managers
    @classmethod
    def menu_gestion_workers(cls):
        print("Menú gestión de trabajadores")
        print("-. 1 Añadir un trabajador")
        print("-. 2 Eliminar un trabajador")
        print("-. 3 Modificar los datos de un trabajador")
        print("-. 4 Mostrar trabajadores del sistema")
        print("-. 5 Asignar usuario de inicio de sesison a trabajador")
        print("-. 6 Cancelar")
        opcion = int(input("¿Que quieres hacer?: "))
        if opcion == 1:
            cls.limpiar_pantalla()
            Worker_User.añadir_worker()
        elif opcion == 2:
            cls.limpiar_pantalla()
            Worker_User.borrar_worker()
        elif opcion == 3:
            cls.limpiar_pantalla()
            Worker_User.modificar_usuario_worker()
        elif opcion == 4:
            cls.limpiar_pantalla()
            Worker_User.mostrar_workers()
        elif opcion == 5:
            cls.limpiar_pantalla()
            Usuario.asignar_worker_usuario()
        elif opcion == 6:
            cls.limpiar_pantalla()
            print("Volviendo al menu principal")
            cls.menu_final_manager()
    
    #definimos un menu para gestionar los managers siendo un administrador
    @classmethod
    def menu_gestion_managers(cls):
        print("Menu de gestion de managers")
        print("-. 1 Crear un Manager")
        print("-. 2 Eliminar un Manager")
        print("-. 3 Modificar los datos de un manager")
        print("-. 4 Mostrar Managers en el sistema")
        print("-. 5 Asignar usuario de inicio de sesión a un manager")
        print("-. 6 Volver al menu principal")
        opcion = int(input("¿Qué quieres hacer?: "))
        if opcion == 1:
            cls.limpiar_pantalla()
            Manager_User.añadir_manager()
        elif opcion == 2:
            cls.limpiar_pantalla()
            Manager_User.borrar_manager()
        elif opcion == 3:
            cls.limpiar_pantalla()
            Manager_User.modificar_usuario_manager()
        elif opcion == 4:
            cls.limpiar_pantalla()
            Manager_User.mostrar_managers()
        elif opcion == 5:
                cls.limpiar_pantalla()
                Usuario.asignar_manager_usuario()
        elif opcion == 6:
            cls.limpiar_pantalla()
            print("Volviendo al menu principal")
            cls.menu_final_administrador()
    
    #definimos un menu para gestionar las tareas siendo manager
    @classmethod
    def menu_gestion_tareas(cls):
        print("Menu gestion de tareas")
        print("-. 1 Crear tarea")
        print("-. 2 Eliminar tarea")
        print("-. 3 Modificar tarea")
        print("-. 4 Mostrar tareas existentes")
        print("-. 5 Asignar tarea a trabajador")
        print("-. 6 Eliminar trabajador de una tarea")
        print("-. 7 Salir")
        opcion = int(input("¿Que quieres hacer?: "))
        if opcion == 1:
            cls.limpiar_pantalla()
            Tarea.añadir_tarea()
        elif opcion == 2:
            cls.limpiar_pantalla()
            Tarea.eliminar_tarea()
        elif opcion == 3:
            cls.limpiar_pantalla()
            Tarea.modificar_datos_tarea()
        elif opcion == 4:
            cls.limpiar_pantalla()
            Tarea.mostrar_tareas()
        elif opcion == 5:
            cls.limpiar_pantalla()
            Tarea.asignar_trabajador_a_tarea()
        elif opcion == 6:
            cls.limpiar_pantalla()
            Tarea.eliminar_trabajador_de_tarea()
        elif opcion == 7:
            cls.limpiar_pantalla()
            print("Volviendo al menu principal")
            cls.menu_final_manager()
    
    #definimos un menu para gestionar los proyectos siendo un manager
    @classmethod
    def menu_gestion_proyectos(cls):
        print("Menu gestion de proyectos")
        print("-. 1 Crear proyecto")
        print("-. 2 Eliminar un proyecto")
        print("-. 3 Modificar datos de un proyecto")
        print("-. 4 Volver al menu principal")
        opcion = int(input("¿Que quieres hacer?: "))
        if opcion == 1:
            cls.limpiar_pantalla()
            Proyecto.crear_proyecto()
        elif opcion == 2:
            cls.limpiar_pantalla()
            Proyecto.eliminar_proyecto()
        elif opcion == 3:
            cls.limpiar_pantalla()
            Proyecto.editar_proyecto()
        elif opcion == 4:
            cls.limpiar_pantalla()
            print("Volviendo al menu principal")
            cls.menu_final_manager()
        
    #definimos un menu para las gestiones de un administrador
    @classmethod
    def menu_gestiones_administrador(cls):
        print("Menu gestiones administrador")
        print("-. 1 Crear administrador")
        print("-. 2 Eliminar administrador")
        print("-. 3 Modificar administrador")
        print("-. 4 Mostrar administradores creados")
        print("-. 5 Crear un usuario de inicio de sesion")
        print("-. 6 Asignar usuario de inicio de sesión a administrador")
        print("-. 7 Volver al menu principal")
        opcion = int(input("¿Que quieres hacer?"))
        if opcion == 1:
            cls.limpiar_pantalla()
            Administrador_User.añadir_administrador()
        elif opcion == 2:
            cls.limpiar_pantalla()
            Administrador_User.borrar_administrador()
        elif opcion == 3:
            cls.limpiar_pantalla()
            Administrador_User.modificar_usuario_administrador()
        elif opcion == 4:
            cls.limpiar_pantalla()
            Administrador_User.mostrar_administradores()
        elif opcion == 5:
            cls.limpiar_pantalla()
            Usuario.agregar_usuario()
        elif opcion == 6:
            cls.limpiar_pantalla()
            Usuario.asignar_admin_usuario()
        elif opcion == 7:
            cls.limpiar_pantalla()
            print("Volviendo al menu principal")
            cls.menu_final_administrador()
            
      
    #Definimos una funcion que limpie la pantalla
    @classmethod
    def limpiar_pantalla(cls):
        os.system('cls' if os.name=='nt' else 'clear')
        
    #definimos un objeto de tipo usuario y lo añadimos a la lista
    usuario1 = Usuario("U1", "admin", "admin", "administrador","UA1")
    usuario2 = Usuario("U2", "manager", "manager", "manager","UM1")
    usuario3 = Usuario("U3", "worker", "worker", "worker","UW1")
    Usuario.lista_usuarios.append(usuario1)
    Usuario.lista_usuarios.append(usuario2)
    Usuario.lista_usuarios.append(usuario3)