print('Bienvenido al Comparador de Edad mas preciso del mundo')
print('Pruebalo Ahora')

Primer_Nombre = input('¿Cual es tu nombre?: ')
Edad_Persona1 = int(input('Introduce tu edad: '))
Segundo_Nombre = input('¿Cual es tu nombre?: ')
Edad_Persona2 = int(input('Introduce tu edad: '))

if Edad_Persona1 > Edad_Persona2:
    print(f'He aqui el resultado, {Primer_Nombre} es mayor que {Segundo_Nombre}')
elif Edad_Persona1 < Edad_Persona2:
    print(f'He aqui el resultado, {Segundo_Nombre} es mayor que {Primer_Nombre}')
else:  
    print(f" El resultado es {Primer_Nombre} y {Segundo_Nombre}, ambos tienen la misma edad amigo ")
