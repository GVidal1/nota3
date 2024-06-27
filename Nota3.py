#Utilidades de funciones y menus
from utilidades import  *
#Guarda la inforamcion de cada estudiante indipendiente


print('Bienvenido a Libro Virtual.')
def main():
  iniciar_sesion()
  while True:
    consultar_menu()
    opcion = int(input('Ingrese alguna opción anterior: '))
    
    if opcion == 1:
      print(f'Usted ha seleccionado {menu[opcion-1]}')
      registrar_alumno(estudiantes)
    elif opcion == 2:
      print(f'Usted ha seleccionado la opción: {menu[opcion-1]}')
      ingresar_nota(estudiantes)
    elif opcion == 3:
      print(f'Usted ha seleccionado la opción: {menu[opcion-1]}')
      (estudiantes)
    elif opcion == 4:
      print(f'Usted ha seleccionado {menu[opcion-1]}')
      mostrar_informacion(estudiantes)
    elif opcion == 5:
      print('Gracias por ocupar el Libro Virtual!')
      break
    else:
      print('Opción inválida, por favor intente de nuevo.')

if __name__ == '__main__':
  main()
