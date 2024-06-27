menu = ['Ingresar alumno o modificar alumno', 'Ingresar o modificar nota', 'Eliminar Estudiante', 'Consultar Alumno', 'Salir']

estudiantes = []

def consultar_menu():
  for cont, elemento in enumerate(menu, start=1):
    print(cont, '-' ,elemento)

def iniciar_sesion():
  valid_user = 'admin'
  valid_passwrod = '12345'
  usuario_ingresado = False
  cont = 5
  while True:
    while cont > 0:
      usuario = input('Ingrese el nombre de usuario: ')
      if usuario == valid_user:
        print('Usuario correcto.')
        usuario_ingresado = True
        break
      else:
        print('usuario incorrecto. Intente Nuevamente.')
        cont -= 1
      if cont == 0:
        print('Ha superado los intentos disponibles. Vuelva a iniciar el programa para volver a intentarlo.')
        break
    while True & usuario_ingresado == True:
      password = input('Ingrese la contraseña: ')
      if password == valid_passwrod:
        print('Contraseña valida.')
        break
      else:
        print('Contraseña inválida. intente nuevamente.')
        cont -= 1
      if cont == 0:
        print('Ha superado los intentos disponibles. Vuelva a iniciar el programa para volver a intentarlo.')
        break
    break
def registrar_alumno(estudiantes):
  while True:
    rut = input('Ingrese el RUT del alumno en formato 123456789 (sin puntos ni guión) para ingresar o modificar un alumno: ')
    if len(rut) > 8 and rut.isdigit():
        break
    else:
        print('Formato inválido. Ingrese otro.')
  
  while True:
    nombre_apellido = input('Ingrese el nombre y apellido del alumno: ').title()
    if not nombre_apellido.replace(' ', '').isalpha():
        print('Valor inválido.')
    else:
        break
  
  curso = input('Ingrese el curso o sección del alumno: ').upper()
  
  alumno = {
    'rut': rut,
    'nombre_apellido': nombre_apellido,
    'curso': curso,
    'nota': ''
  }
  
  estudiantes.append(alumno)
  print('Registro de alumno exitoso.')


def ingresar_nota(estudiantes):
  buscar = input('Ingrese el RUT (formato: 123456789) del alumno a consultar: ')
  encontrado = False

  for alumno in estudiantes:
    if alumno['rut'] == buscar:
        encontrado = True
        opcion = input('Ingrese 1 para ingresar nota\nIngrese 2 para modificar nota\nIngrese aquí: ')
        
        if opcion == '1':
            if alumno['nota']:
                print(f'Notas del alumno {alumno["nombre_apellido"]}:')
                print(alumno['nota'])
            else:
                print(f'No se han registrado notas para el alumno {alumno["nombre_apellido"]}.')
            
            nota = input('Ingrese la nota del alumno: ')
            alumno['nota'] += f'\n{nota}' if alumno['nota'] else nota
            print(f'Notas del alumno {alumno["nombre_apellido"]}: {alumno["nota"]}')
        
        elif opcion == '2':
            modificar_nota(alumno)
        
        else:
            print('Opción inválida.')
        
        break

  if not encontrado:
      print('No se ha encontrado el RUT ingresado.')

def modificar_nota(alumno):
  if alumno['nota']:
    print(f'Notas actuales del alumno {alumno["nombre_apellido"]}:')
    print(alumno['nota'])
    nueva_nota = input('Ingrese la nota modificada del alumno: ')
    alumno['nota'] = nueva_nota
    print(f'Nota modificada correctamente.')
  else:
    print(f'No se han registrado notas para el alumno {alumno["nombre_apellido"]}. No se puede modificar.')
    
def eliminar_estudiantes(estudiantes):
  buscar = input('Ingrese el RUT del alumno a eliminar: ')
  encontrado = False

  for i, alumno in enumerate(estudiantes):
      if alumno['rut'] == buscar:
          encontrado = True
          del estudiantes[i]
          print('Estudiante eliminado.')
          break

  if not encontrado:
      print('Estudiante no encontrado.')

def mostrar_informacion(estudiantes):
  buscar = input('Ingrese el RUT (formato 123456789) del alumno a consultar: ')
  encontrado = False
  
  for alumno in estudiantes:
    if alumno['rut'] == buscar:
        encontrado = True
        print(f'Alumno {alumno["nombre_apellido"]}\nRUT: {alumno["rut"]}\nCurso/Sección: {alumno["curso"]}\nNotas: {alumno["nota"]}\n')
        break
  
  if not encontrado:
    print('No se ha encontrado el RUT ingresado.')
