
class Copo:
    # função init define como o copo é.
    def __init__(self):
        self.cor = "Transparente"
        self.volume = 190
        self.material = "Vidro"
        self.liquido = "Cerveja"
    
    # Ação de encher o copo
    def encher(self):
        print(f"O copo está cheio de {self.liquido}")
        print(f"Volume do copo: {self.volume} ml.")
    