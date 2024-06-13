#Utilidades de funciones y menus
from utilidades import  *
#Guarda la inforamcion de cada estudiante indipendiente
estudiantes = []

print('Bienvenidos a Libro Virtual')
while True:
  consultar_menu()
  opcion = int(input('Ingrese alguna opción anterior: '))
  #opcion1 en menu (utilidades): crea un estudiante nuevo en la base de datos y los guarda en la lista de estudiantes
  if opcion == 1:
    print(f'Usted ha seleccionado {menu[opcion-1]}')
    while True:
      rut = input('Ingrese el RUT del alumno en formato 123456789 (sin puntos ni guión) para ingresar o modificar un alumno: ')
      if (len(rut) > 8) and (rut[:].isdigit()):
        break
      else:
        print('Formato inválido. Ingrese otro')
    while True:
      nombre_apellido = input('Ingrese el nombre y apellido del alumno: ').title()
      if nombre_apellido == nombre_apellido.isdigit():
        print('Valor invalido')
      else:
        break
    curso = input('Ingrese el curso o sección del alumno: ').upper()
    alumno = {
      'rut': rut,
      'nombre_apellido': nombre_apellido,
      'curso': curso,
      'nota': '',
      'anotaciones': '',}
    estudiantes.append(alumno)
    print('Registro de alumno exitoso.')
  if opcion == 2:
    print(f'Usted a seleccionado la opción: {menu[opcion-1]}')
    buscar = input('Ingrese el RUT (formato: 123456789) del alumno a consultar: ')
    encontrado = False
    for alumno in estudiantes:
      if alumno['rut'] == buscar:
        encontrado = True
        if 'nota' in estudiantes:
          print(f'Notas del alumno {alumno["nombre_apellido"]:}')
          print(alumno['nota'])
        else:
          print(f'No se han registrado notas para el alumno {alumno["nombre_apellido"]}')
        nota = input('Ingrese la nota del alumno: ')
        if 'nota' in alumno:
          alumno['nota'] += f'\n{nota}'
        else:
          alumno['nota'] = f'{nota}'
        print(f'Notas del alumno {alumno["nombre_apellido"]}: {alumno["nota"]}')
        break
      if not encontrado:
        print('No se ha encontrado el RUT ingresado.')
  #opcion4: Muestra el registro de cada estudiante y su informacion ingresada.
  if opcion == 4:
    print(f'Usted a seleccionado {menu[opcion-1]}')
    buscar = input('Ingrese el RUT (formato 123456789) del alumno a consultar: ')
    encontrado = False
    for alumno in estudiantes:
      if alumno['rut'] == buscar:
        print(f'Alumno {alumno["nombre_apellido"]}\nRUT: {alumno["rut"]}\nCurso/Sección: {alumno["curso"]}\nNotas: {alumno["nota"]}\nObservaciones/Anotaciones: {alumno["anotaciones"]}')
      elif not encontrado:
        print('No se ha encontrado el RUT')
  if opcion == 5:
    print('Gracias por ocupar el Libro Virtual!')
    break
