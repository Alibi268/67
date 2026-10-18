# Aqui estamos importando random. Esto nos ayuda a elegir aleatoriamente un elemento de la matriz
import random

# 1:-Comenzamos primero que nada, como en el diagrama de flujo indicamos declarando nuestras 8 listas, donde almacenaremos las palabras para el juego


VideoJuegosN =["Fallout", "Halo","Battlefield","Zelda"]
PaisesN = ["México","Alemania","Italia","Inglaterra","Estados Unidos","Japón","Brasil"]
ComidaN=["Pizza","Hamburguesa","Helado","Pasta","Pozole","Churros","Chocolate","Torta"]
AnimalesN= ["Perro", "Gato", "Caballo", "Serpiente", "Pez", "Tortuga", "Llama"]

VideoJuegosD =[ "Plantas vs Zombies", "Call of Duty", "Resident Evil", "Grand Theft Auto", "Cyberpunk"]
PaisesD =["Azerbaijan", "Jersey","Macedonia del Norte", "Bielorussia", "Islandia", "Cabo Verde"]
ComidaD=["Bruschetta","Croissant", "Paella","Goulash"]
AnimalesD=["Axolotl", "Cheetah","Grizzly", "Capibara" ]

#Vamos a declarar otra lista donde vamos a ALMACENAR las LISTAS que si vamos a usar dependiendo de lo que eliga el usuario
PalabrasAUsar= []

#Aquí imprimimos nuestro menú
print("""
+---------------------------------------------+
    Bienvenido a el juego de Ahorcado
        Ingresa tu nombre/alias:

+----------------------------------------------+
""")

#Aquí declaramos nuestra variable Nombre, el cual va a ser el alias/nombre del usuario

Nombre = input("Nombre/Alias: ")

#Imprimimos la primera parte de selección de categoria

print("""
-----------------------------------------
        Selecciona una categoria
          1)Videojuegos
          2)Paises
          3)Comida
          4)Animales
-----------------------------------------
""")

#Ocupamos un while True, para que si se equivoca o quiere cambiar de categoria pueda hacerlo de manera rápida
while True:

#Aquí muy importante, estamos usando lo de try y except para que si el usuario ingresa cosas que no, No nos rompa el programa

#Aquí es ¿Dónde vamos a usar nuestra "excepción" ? Con try intentamos convertir la respuesta del usuario a un número entero.
    try:
        categoria = int(input("Seleccione la categoria: "))

#Aquí verificamos si el número ingresado corresponde a alguna de nuestras 4 categorías.    #Cómo unicamente tenemos 4 categorias disponibles, y para seleccionarlas le pedimos al usuario un numero del 1-4. En caso si coloque algo que NO sea el 1,2,3 o 4. 
        if categoria < 1 or categoria > 4:
            print("Opción no valida")
            continue #Ocupamos continue. Si el número no es válido, volvemos a pedir la categoría

    except ValueError:#Si el usuario escribe letras, int() no puede convertirlas a número y entramos aquí
        print("Error ingrese nuevamente su opción")
        print("""
-----------------------------------------
        Selecciona una categoria
          1)Videojuegos
          2)Paises
          3)Comida
          4)Animales
-----------------------------------------
""")
        continue# Después del error, regresamos al inicio del while

    #Este match está dentro del while, pero fuera del try-except. Sirve para saber qué categoría eligió el jugador.
    match categoria:

        case 1:
            print("Categoria seleccionada: Videojuegos")
            PalabrasAUsar = [VideoJuegosN, VideoJuegosD] #Aquí lo importante a comentar es que cuando ya sabemos que categoria vamos a usar, la lista de palabras A USAR , como estaba vacia, vamos a llenarla con las 2 listas (Normal y dificl) de la categoria que haya elegido el usuario
            #Si nos damos cuenta en todas estas opciones, en la lista la llenamos en el indice 0 con las palabras de dificultad normal y en el indice 1 las palabras dificles
        case 2:
            print("Categoria seleccionada: Paises")
            PalabrasAUsar= [PaisesN, PaisesD] #Lo mismo, llenamos la lista vacia con las que vamos a usar

        case 3:
            print("Categoria seleccionada: Comida")
            PalabrasAUsar= [ComidaN, ComidaD]

        case 4:
            print("Categoria seleccionada: Animales")
            PalabrasAUsar= [AnimalesN, AnimalesD]

# Esto lo implementamos de manera en que antes de jugar, si el usuario quiere cambiar de categoria pueda hacerlo rápido y facil sin tener que volver a ingresar su nombre
        # Repetimos la pregunta hasta que ingrese 1 o 2
    while True:

        correcta = input("""Es correcta su opción?

                    1.-Si

                    2.-No

            Ingrese opción: """)

        if correcta == "1" or correcta == "2":
            break

        else:
            print("Opción no válida, ingrese 1 o 2")


    # Ahora revisamos qué respondió el jugador
    if correcta == "1":
        break

    elif correcta == "2":
        print("Seleccione nuevamente su categoria")
        continue

#Creamos otro while independiente para que el usuario pueda elegir su dificultad.
while True:
    print("""Excelente, ahora escoga la dificultad:
    
                a)Normal

                b)Dificil              
                   """)
#Nueva variable para escoger la dificultad del juego
#Este lo colocamos con el .lower() al final porque quisimos ponerle a) y b) para elegir la dificultad.

    dificultad = input("Eliga la dificultad: ").lower()

    match dificultad:
        case "a":
            print("Ha elegido la dificultad normal ;) ")
            #Aquí, dependiendo de que dificultad haya elegido es que vamos a hacer lo siguiente
            #1.-Declaramos nueva variable donde vamos a guardar la LISTA de palabras que queramos, en el punto anterior vimos que dependiendo de la categoria, la lista PALABRAS A USAR la llenabamos con 2 listas, palabras normales y palabras dificiles
            #2.-Al declarar la nueva variable PALABRAS A ELEGIR = PALABRAS A USAR [0], estamos diciendo: Sin importar la categoria que hayamos elegido, SOLAMENTE VAMOS A OCUPAR LA LISTA DE LAS NORMALES. Porque las normales se encuentran en el subindice 0
            PalabrasElegidas = PalabrasAUsar [0]

        case "b":
            #Aquí como es el caso b), donde el usuario quiere jugar con las palabras dificles, al variable PALABRAS ELEGIDAS va a adoptar el valor de la lista que se encuentra en el subindice 1 de las PALABRAS A USAR (palabras dificiles)
            print("Ha elegido la dificultad dificil " )
            PalabrasElegidas = PalabrasAUsar [1]

        case _:
            print("Opción No valida")
            continue

    break # Este break termina el while de dificultad y permite continuar con el juego.

#Declaramos nuestra variable palabrasecreta y seleccionamos una palabra aleatoria de la lista que escogimos con la herramienta de random que importamos al inicio
PalabraSecreta = random.choice(PalabrasElegidas)

#Vamos a convertir la palabra secreta a mayusuculas
PalabraSecreta = PalabraSecreta.upper()

#Crearemos otra lista apra moestrar los espacios de la palabra

PalabraConGuión = []

#Recorreremos cada caractér de la PALABRASECRETA para que hagamos lo siguiente:

for letra in PalabraSecreta:

    if letra == " ": #Si mi palabra secreta tiene un espacio, no cuente el espacio como un "_"
        PalabraConGuión.append(" ")

    else: #En caso de que si sea una letra, coloque "_"
        PalabraConGuión.append("_")


#Ahora vamos a hacer que cuando nos imprima los guiones bajos, nos lo imprima de manera que no se vea como matriz. Aquí vamos a usar .join.

print("Palabra a adivinar: ", " ".join(PalabraConGuión))

#----------------------------VARIABLES DE GAMEPLAY --------------------------------#

errores = 0
intentosMaximos = 6
letrasUtilizadas = [] #Aquí es donde vamos a guardar las letras que haya usado el jugador para que si las vuelve a colocar no le cuente como intento y le diga que intente con otra, que esa ya la uso.

print("Intentos restantes: ", intentosMaximos - errores) 







