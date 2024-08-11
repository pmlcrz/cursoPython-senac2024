hora = 0
while hora < 24:
    minuto = 0
    while minuto < 60:
        segundo = 0
        while segundo < 60:
            print(f"{hora:02}:{minuto:02}:{segundo:02}")
            segundo += 1
        minuto += 1
    hora += 1
