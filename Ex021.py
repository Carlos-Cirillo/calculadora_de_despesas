import pygame

pygame.init()  # inicializa o pygame

# Carrega o MP3
pygame.mixer.music.load('musica2.mp3')

# Toca o som
pygame.mixer.music.play()

# Mantém o programa rodando até o som terminar
while pygame.mixer.music.get_busy():
    pass
