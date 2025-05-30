
lugares_visitados = []
print("¡Bienvenido/a al tracker de viajes! ✈️🌄\n")

while True:
    lugar = input("📍 ¿Qué lugar de Traslasierra has visitado? (o escribe 'fin'): ")
    if lugar.lower() == 'fin':
        break
    lugares_visitados.append(lugar)

print("\n📌 Tus lugares visitados:", ", ".join(lugares_visitados))
print("¡Gracias por usar el programa! 🎒 Hasta la próxima aventura. 🚀")