def usuario(nombre):
 import re   
 #nombre = input();
 if len(nombre) < 6 :
  print(f"El nombre de usuario debe contener al menos 6 caracteres, {nombre}");
 elif len(nombre)>12 :
  print(f"El nombre de usuario no puede contener más de 12 caracteres, {nombre}");
 elif re.match('\w', nombre):
     return True
 else:
   print(f"El nombre no es alfanumerico , {nombre}");
		
	
