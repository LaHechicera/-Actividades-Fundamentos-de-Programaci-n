"""La empresa eléctrica luz de la mañana, desea crear un interruptor de
escalera digital, tal de que sea programable en un circuito rduino.
La idea es que existan 2 interruptores del tipo On - OFF a cada
extremo de una escalera o pasillo permitiendo que se pueda prender o
apagar de cualquiera de los dos extremos.
La lógica involucrada en esto es de un NOT XOR, es decir, la luz se
prenderá sólo si ambos interruptores están en ON, o si ambos
interruptores están en OFF."""

interruptor1 = 1
interruptor2 = 0

if not(interruptor1 ^ interruptor2):
    print("Prende la luz")
else:
    print("Apaga la luz")