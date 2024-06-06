# Reprodutor de música - T-800
import pygame
import time

pygame.init()
pygame.mixer.music.load('musicas/rhblues.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.9) # Escolha o volume de 0 a 9

# Aguarde até que a música termine de tocar
while pygame.mixer.music.get_busy():
    time.sleep(1)

# Encerre o mixer e finalize o programa
pygame.mixer.quit()
print('Caramba, que música incrível! Quem sabe qual será a próxima música?')
print('teste github')

