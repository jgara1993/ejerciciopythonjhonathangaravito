def clave(contrasena):
  import re;
  #print("¿Ingrese la contraseña?");
  #contrasena = input()
  validar=False
  mayuscula=False
  minuscula=False
  numeros=False
  y=contrasena.isalnum()
  correcto=True
  espacio=False
    
  for carac in contrasena: #ciclo for que recorre caracter por caracter en la contraseña
    if carac.isspace()==True:
      espacio=True
    if carac.isupper()== True: #saber si hay mayuscula
      mayuscula=True #acumulador o contador de mayusculas
    if carac.islower()== True: #saber si hay minúsculas
      minuscula=True #acumulador o contador de minúscula
    if carac.isdigit()== True: #saber si hay números
      numeros=True #acumulador o contador de numero
    
    
  if len(contrasena)<8 :
    print("La contraseña debe tener minimo 8 caracteres");
  elif espacio == True :
    print("La contraseña no puede tener espacios en blanco");
  elif mayuscula == True and minuscula ==True and numeros == True:
    validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
  else:
    correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
  if correcto == False:
    print("La contraseña elegida no es segura")
  elif validar == True:
    return True
