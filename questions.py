import random
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# respuestas que debe ingresar el usuario
response = ["1","2","3","4"]
# inicializacion del puntaje
score = float(0)
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#inicialiacion de la lista que contiene cada pregunta, opciones y respueta por intento aleatoriamente 
questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for i in questions_to_ask:
    print(f"su puntaje es {score}")
    # Se muestra la pregunta y las respuestas posibles
    print(i[0])
    for j,answer in enumerate(i[1]):
        print(f"{j+1}.{answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: ")) 
        #se verifica que la respuesta sea valida para evaluar
        is_valid = False
        for a in response:
            if (a == user_answer):
                #si es una respuesta valida y se realiza la conversion de la respueta a int
                is_valid = True
                user_answer = int(user_answer) - 1 
        #si el usuario no ingreso una respuesta valida, se termina el proograma y se notifica al usuario
        if (not is_valid):
            print("respuesta no valida")
            exit(1)
        #se evalua si la respuesta es correcta y se suma 1 punto
        elif user_answer == i[2]:
            print("¡Correcto!")
            score +=1
            break
        #el usuario fallo y se le resta 0.5 puntos
        else:
            score -=0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(i[1][i[2]])
        # Se imprime un blanco al final de la pregunta
        print()
print(f"el puntaje total es de {score} ")
