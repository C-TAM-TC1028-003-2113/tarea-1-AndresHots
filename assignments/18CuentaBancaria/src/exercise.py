def main():
    # escribe tu código abajo de esta línea
     x1 = float(input("Ingrese el salgo del mes antrior: "))
    ing = float(input("Ingresos: "))
    egr = float(input("egresos: "))
    numCheq = int(input("Ingrese el numero de cheques expedidos: "))
    interes= .75

    total = ( x1 + ing + egr + (numCheq*13) ) * interes

    print("El saldo final de la cuenta es: $", total)


if __name__ == '__main__':
    main()
