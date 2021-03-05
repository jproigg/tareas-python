print('Tienda Simon Jose Pablo Roig')

import os
import sys


def es_admin(usuario):
    return usuario['role'] == 'admin'
    
    
def es_invitado(usuario):
    return usuario['role'] == 'invitado'


def existe_usuario(usuario, username, password):
    return usuario['username'] == username and usuario['password'] == password


def consulta_productos(departamento):
    productos = empresa['departamentos'][departamento]['productos']
    
    if len(productos) == 0:
        print('No hay productos')
    else:
        for producto in productos:
            print(f"codigo: {producto['codigo']}")
            print(f"nombre: {producto['nombre']}")
            print(f"precio: {producto['precio']}")
            print(f"cantidad: {producto['cantidad']}")


def agrega_producto(departamento):

    nombre = input('Digite el nombre del producto ')
    codigo = int(input('Digite el codigo del producto '))
    precio = float(input('Digite el precio del producto '))
    cantidad =  int(input('Digite la cantidad '))

    productos = {
    "nombre": nombre,
    "precio": precio,
    "codigo": codigo,
    "cantidad": cantidad,
  }
    
    empresa['departamentos'][departamento]['productos'].append(productos)


def actualiza_producto(departamento):

    productos = empresa['departamentos'][departamento]['productos']

    codigo = int(input('Digite el codigo del producto '))
    for producto in productos:
        if codigo == producto['codigo']:

            nombre = input('Digite el nombre del producto ')
            precio = float(input('Digite el precio del producto '))
            cantidad =  float(input('Digite la cantidad '))
            
            producto['nombre'] = nombre
            producto['precio'] = precio
            producto['cantidad'] = cantidad

        else:
            print('codigo invalido intente nuevamente')
            
        


    



def menu_main():

    if es_admin(usuario_conectado):
        opcion = int(input('''Seleccione un departamento:
1- Damas
2- Caballeros
3- Niños
4- Salir
Digite el numero de su opcion: '''))
        if opcion == 1:
            os.system('cls')
            menu_de_departamentos('damas')
        elif opcion == 2:
            os.system('cls') 
            menu_de_departamentos('caballeros')
        elif opcion == 3:
            os.system('cls') 
            menu_de_departamentos('niños')
        elif opcion == 4:
            os.system('cls') 
            sys.exit()
        else:
            os.system('cls') 
            menu_main()
    elif es_invitado(usuario_conectado):
        opcion = int(input('''Seleccione un departamento:
1- Damas
2- Caballeros
3- Niños
Digite el numero de su opcion: '''))
        if opcion == 1:
            os.system('cls') 
            menu_de_departamentos('damas')
        elif opcion == 2:
            os.system('cls') 
            menu_de_departamentos('caballeros')
        elif opcion == 3:
            os.system('cls') 
            menu_de_departamentos('niños')
        else:
            sys.exit()


def menu_de_departamentos(departamento):
    if es_admin(usuario_conectado):
        opcion = int(input(f'''Menú de productos del departamento de {departamento}: 
1-Consultar
2-Ingresar 
3-Actualizar 
4-Eliminar  
5-Volver 
6-Salir 
Digite el numero de su opcion: ''' ))
        if opcion == 1:
            os.system('cls')
            print('Consulta de productos')
            consulta_productos(departamento)
            menu_de_departamentos(departamento)          
        elif opcion == 2:
            os.system('cls')
            print('ingrese el producto ')
            agrega_producto(departamento)
            menu_de_departamentos(departamento)           
        elif opcion == 3:
            os.system('cls')
            print('actualice el producto')
            actualiza_producto(departamento)
            menu_de_departamentos(departamento)           
        elif opcion == 4:
            os.system('cls')
            print('elimine el producto')
            menu_de_departamentos(departamento)             
        elif opcion == 5:
            os.system('cls')
            menu_main()
            os.system('cls')
            
            
        elif opcion == 6:
            os.system('cls')
            print('Saliendo del sistema de inventarios')
            sys.exit()
        else:
            os.system('cls')
            print('Opcion invalida')
            menu_de_departamentos(departamento) 
    elif es_invitado(usuario_conectado):
        opcion = int(input(f'''Menú de productos del departamento de {departamento}: 
1-Consultar  
2-Volver 
3-Salir 
Digite el numero de su opcion: ''' ))
        if opcion == 1:
            os.system('cls')
            print('Consulta de productos')
            consulta_productos(departamento)
            menu_de_departamentos(departamento)
        elif opcion == 2:
            os.system('cls')
            menu_main()
        elif opcion == 3:
            os.system('cls')
            print('Saliendo del sistema de inventarios')
            sys.exit()
        else:
            os.system('cls')
            print('Opcion invalida')
            menu_de_departamentos(departamento)

           
empresa = {
  "nombre_tienda": "Tienda Simon",
  "sede": "Escazu",
  "departamentos": {
    "damas": { "productos": []},
    "caballeros": { "productos": []},
    "niños": { "productos": []}
  }
}

   
usuarios = [
    {
        "username": "admin",
        "password": "admin",
        "full_name": "Alejandro Sanchez",
        "role": "admin"
    },
    {
        "username": "guest",
        "password": "guest",
        "full_name": "Jose Pablo Roig",
        "role": "invitado"
    }
]

 
username = input('Digite su nombre de usuario: ')
password = input('Digite su contraseña: ')

usuario_conectado = None

for usuario in usuarios:
    if existe_usuario(usuario, username, password):
        usuario_conectado = usuario
        break


if not usuario_conectado:
    print('Programa finalizado')
    sys.exit()

os.system('cls') 
    
print(f"Bienvenido al sistema de inventarios de tienda Simón, {usuario_conectado['full_name']} es un placer atenderle")


if es_admin(usuario_conectado):
    inventario = input('Desea ingresar al sistema de inventarios(si/no):  ')
    if inventario == ('si'):
        os.system('cls')
        menu_main()
    elif inventario == ('no'):
        os.system('cls')
        print('programa finalizado')
        sys.exit()
    else:
        os.system('cls')
        print('opcion no es valida')
        sys.exit()
elif es_invitado(usuario_conectado):
    inventario = input('Desea ingresar al sistema de inventarios(si/no):  ')
    if inventario == ('si'):
        os.system('cls')
        menu_main()
    elif inventario == ('no'):
        os.system('cls')
        print('Programa finalizado')
        sys.exit()
    else:
        os.system('cls')
        print('opcion no es valida')
        sys.exit()
        



  










    



