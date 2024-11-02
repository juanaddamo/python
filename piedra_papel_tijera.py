jugador_1 = input("Jugador 1: Ingrese piedra --> pi, papel -->pa o tijera --> ti: ")
jugador_2 = input("Jugador 2: Ingrese piedra --> pi, papel -->pa o tijera --> ti: ")

if jugador_1 == "pi" and jugador_2 == "pa":
    print ("Gana Jugador 2 --> Papel le gana a Piedra")

if jugador_1 == "pa" and jugador_2 == "ti":
    print ("Gana Jugador 2 --> Tijera le gana a Papel")

if jugador_1 == "ti" and jugador_2 == "pi":
    print ("Gana Jugador 2 --> Piedra le gana a Tijera")

if jugador_1 == "pa" and jugador_2 == "pi":
    print ("Gana Jugador 1 --> Papel le gana a Piedra")

if jugador_1 == "ti" and jugador_2 == "pa":
    print ("Gana Jugador 1 --> Tijera le gana a Papel")

if jugador_1 == "pi" and jugador_2 == "ti":
    print ("Gana Jugador 1 --> Piedra le gana a Tijera")

