menu = ['Ingresar alumno', 'Ingresar nota', 'ingresar Anotacion', 'Consultar Alumno', 'Salir']

def consultar_menu():
  for cont, elemento in enumerate(menu, start=1):
    print(cont, '-' ,elemento)