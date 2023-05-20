import time, random, sys

print("El más rápido del oeste")
print("Es hora de poner a prueba tus reflejos")
print(" Cuando veas el mensaje 'DISPARA', tienes 0.3 segundos para presionar ENTER")
print("Pero si presionas antes del mensaje o despues (del tiempo establecido) tu PIERDES")
input("Presiona la tecla Enter para continuar ...")

while True:
    print("Es medio dia y todo el pueblo esta escondido, esperando el momento de la acción")
    time.sleep(random.randint(20,50)/10.0)
    print("DISPARA")
    tiempo_disparo = time.time()
    input()
    tiempo_transcurrido = time.time() - tiempo_disparo

    if tiempo_transcurrido < 0.01:
        print("Disparaste antes de que apareciera el mensaje. Tu pierdes :()")
    elif tiempo_transcurrido > 0.3:
        tiempo_transcurrido = round(tiempo_transcurrido, 4)
        print(f"Tomaste {tiempo_transcurrido} segundos para disparar. Muy lento, ¡Perdiste!")
    else:
        tiempo_transcurrido = round(tiempo_transcurrido, 4)
        print(f"Tomaste {tiempo_transcurrido} segundos para disparar.")
        print("Eres el más rápido del oeste. ¡Tu ganas!")

    print("Ingrese Q para salir o presione ENTER para jugar de nuevo")
    respuesta = input(">").upper()
    if respuesta == 'Q':
        print("Gracias por jugar")
        sys.exit()
