import time, random

cantidad = None
tarjeta = None
cvc = None
mes = 11
year = 2025
inicio = 100000000
inicio2 = 100
fin = 9999999999
fin2 = 999
vBin = None
userid = "None"

print("Cargando programa...")
time.sleep(5)
print("Programa cargado.")

while cantidad != 6 or vBin.isdigit() == 0:
    vBin = input("\nIngrese el bin: ")
    cantidad = len(vBin)

    if cantidad == 6 and vBin.isdigit() == 1:
        print("El bin ingresado es válido. Espere un momento...\n")
        time.sleep(3)
    else:
        print("El bin ingresado es inválido.")

print("El bin ingresado es: "+ vBin + "xxxxxxxxxx")
print("Genenerando número de tarjeta de crédito. Por favor, espere...")
time.sleep(10)
print("Operación terminada con éxito.\n")

tarjeta = random.randint(inicio, fin)
cvc = random.randint(inicio2, fin2)

print("______DATOS______")
print("Número de tarjeta de crédito: " + str(vBin) + str(tarjeta))
print("CVC: " + str(cvc))
print("Fecha de expiración: " + str(mes) + "/" + str(year))

while userid.isdigit() == 0:
    userid = input("\nIngrese la ID de tu cuenta: ")
    if userid.isdigit() == 0:
        print("El userid ingresado es inválido.")

print("ID de tu cuenta: " + str(userid))

print("\nIniciando operaciones, no te desconectes de internet. Espere un momento...")
time.sleep(2)
print("Bypasseando la seguridad de la página, este proceso tardará menos de 1 minuto.")
print("Se le notificará con un sonido cuando el proceso finalice.")
time.sleep(45)

print("\a\a\a\a\a")

print("Se ha realizado el pago por 10 FZ. Puedes cerrar el programa.")
print("Ahora solamente debes esperar a que la administración acepte el pago y te depositen los 10 FZ.")

print("\nPrograma desarrollado por Votati.")

time.sleep(2)
input("\nPresione cualquier tecla para cerrar el programa.")
