from cliente_dao import ClienteDAO
from cliente import Cliente
seleccion = None
while seleccion != 5:
    print(f'''
    |CLIENTES ZONA FIT (GYM)|
     ***MENÚ DE OPCIONES ***
    1. Mostrar base de datos de clientes.
    2. Agregar nuevo cliente.
    3. Modificar datos del cliente.
    4. Eliminar datos del cliente.
    5. Salir. ''')
    seleccion = int(input('Introduce la opción que desee: '))  

    if seleccion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n |Lista de clientes del gimnasio|')
        for cliente in clientes:
            print(cliente)
    elif seleccion == 2:
        nombre_var = input('Introduce el nombre: ')
        apellido_var = input('Introduce el apellido: ')
        membresia_var = input('Introduce la membresía: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresía=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    
    elif seleccion == 3:
        id_cliente_var = int(input('Escribe el id del cliente a modificar: '))
        nombre_var = input('Escribe el nombre del cliente: ')
        apellido_var = input('Escribe el apellido: ')
        membresía_var = input('Escribe la membresía: ')
        cliente = Cliente(id=id_cliente_var, nombre=nombre_var, apellido=apellido_var, membresía=membresía_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')

    elif seleccion == 4:
        id_cliente_eliminado = int(input('Introduce el id del cliente que desee eliminar:'))
        cliente = Cliente(id=id_cliente_eliminado)
        cliente_eliminado = ClienteDAO.eliminar(cliente)
        print(f'Se ha eliminado los siguientes clientes: {cliente_eliminado}')
    else:
        print('Salimos de la aplicación...')