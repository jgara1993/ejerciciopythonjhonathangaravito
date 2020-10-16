import usuario
import contraseña
correcto=False
while correcto==False:
  nombre=input("Ingrese nombre de usuario: ")
  if usuario.usuario(nombre) == True:
    print("Usuario creado exitosamente")
    correcto=True
while correcto==True:
  contrasenia=input("Ingrese su Contraseña: ")
  if contraseña.clave(contrasenia) == True :
    print("Contraseña creada exitosamente")
    correcto=False
