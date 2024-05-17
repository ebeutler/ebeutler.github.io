# Bibliothek die ein einfaches Programmieren von Spielen ermöglicht
import pygame
# Ermöglicht einen einfacheren Zugriff auf Variablen wie z.B. QUIT
from pygame.locals import *

pygame.init() # Startet das Spielfenster

# Definiert die grösse des Fensters und speichert dieses in einer Variable
FENSTER_BREITE = 1200
FENSTER_HOEHE = 675
FENSTER = pygame.display.set_mode((FENSTER_BREITE, FENSTER_HOEHE))

# Setzt den Titel des Fensters
pygame.display.set_caption("<Titel einfügen>")

# Limitiert die Anzahl maximal gezeichneten Bilder pro Sekunde
FPS = 60
pygame.time.Clock().tick(FPS)

# Unendlich laufende Hauptschleife (Läuft so lange wie das Programm).
while True:
    for event in pygame.event.get(): # Verarbeite alle aufgetretenen Ereignisse
        if event.type == QUIT: # Prüft ob das aufgetretene Ereignis ein "Schliessen" ist
            pygame.quit() # Schliesst das Fenster
            exit() # Beendet das Programm
    
    # ... Hier kommt dein Code
    
    # Zeichnet das Fenster neu
    pygame.display.update()