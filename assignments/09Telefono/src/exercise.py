def main():
    # escribe tu código abajo de esta línea
     sms = int(input("Ingrese el numero de mensajes enviados: "))
    mega = float(input("Ingrese el numero de megas consumidos: "))
    minu = int(input("Ingrese el numero de minutos: "))
    
    costo = (0.80*sms) + (0.80*mega) + (0.80*minu)
   
print("El costo mensual es de: $",costo, "pesos")

if __name__ == '__main__':
    main()
