def main():
    # escribe tu código abajo de esta línea
   # escribe tu código abajo de esta línea
    nuevo = int(input("Ingrese la cantidad de juegos nuevos a adquirir: "))
    usado = int(input("Ingrese la cantidad de juegos usados a adquirir: "))

    total = (1000 * nuevo) + (350 * usado)

    print("El monto total a pagar es de: $", total )


if __name__ == '__main__':
    main()
