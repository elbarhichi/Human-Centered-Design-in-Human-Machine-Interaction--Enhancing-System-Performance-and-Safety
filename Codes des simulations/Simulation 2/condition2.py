import pygame
import sys
import math

# Fréquence cardiaque en battements par minute (BPM)
f = 100

# Fréquence cardiaque en battements par seconde (BPS)
fs = f / 60

# Période d'un battement en secondes (Ts)
Ts = 1 / fs

# Durée totale du mouvement de la bille en secondes
total_duration = 29

# Calcul du nombre de va-et-vient
number_of_bips = math.ceil(total_duration / Ts)

print("Nombre de clignottements et bips:", number_of_bips)

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Définition de la taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simulation du carré clignotant et bipant")

# Création du carré clignotant
square_size = 200
square_color = WHITE
square_x = (WINDOW_WIDTH - square_size) // 2
square_y = (WINDOW_HEIGHT - square_size) // 2

# Variables de temporisation pour le clignotement du carré
square_visible = False
beep_sound = pygame.mixer.Sound("beep.wav")

# Variables de temporisation entre les clignotements
inter_blink_delay = (int(Ts * 1000)//2)


# Chargement des images
image1 = pygame.image.load("image1.jpg")
image2 = pygame.image.load("image2.jpg")
image3 = pygame.image.load("image3.jpg")

# Position des images en haut à droite
image_position = (50, 20 )

# Variables de temporisation pour afficher les images
image1_time = 5 * 1000  # Temps en millisecondes (5s)
image2_time = 13 * 1000  # Temps en millisecondes (13s)
image3_time = 21 * 1000  # Temps en millisecondes (21s)

# Variables pour garder une trace de l'affichage des images
image1_displayed = False
image2_displayed = False
image3_displayed = False


# Création d'un bouton "Démarrer"
button_width = 200
button_height = 50
start_button = pygame.Rect((WINDOW_WIDTH - button_width) // 2, WINDOW_HEIGHT - button_height - 50, button_width, button_height)

# Police de texte pour le bouton
font = pygame.font.Font(None, 36)

# Variables de temporisation
start_time = None
start_button_visible = True

# Boucle principale
running = True
simulation_started = False
bips_count = 0  # des bips
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if start_button.collidepoint(mouse_pos):
                simulation_started = True
                start_time = pygame.time.get_ticks()
                last_blink_time = start_time  # Enregistrement du moment du clic

    # Si la simulation a démarré
    if simulation_started:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  # Démarrage du mouvement après 1 seconde
            square_visible = not square_visible
            last_blink_time = current_time
            bips_count += 1  # Incrémentation du compteur de bips

            # Vérification si le nombre de bips prévu est atteint
            if bips_count >= number_of_bips*2:
                running = False  # Arrêt du jeu


        # Affichage des images aux moments spécifiés
        if current_time - start_time >= image1_time and not image1_displayed:
            image1_displayed = True

        if current_time - start_time >= image1_time + 5 * 1000 :
            image1_displayed = False


        if current_time - start_time >= image2_time and not image2_displayed:
            image2_displayed = True

        if current_time - start_time >= image2_time + 5 * 1000 :
            image2_displayed = False


        if current_time - start_time >= image3_time and not image3_displayed:
            image3_displayed = True

        if current_time - start_time >= image3_time + 5 * 1000 :
            image3_displayed = False


        # Effacement de l'écran
        window.fill(BLACK)

        if image1_displayed:
            window.blit(image1, image_position)

        if image2_displayed:
            window.blit(image2, image_position)

        if image3_displayed:
            window.blit(image3, image_position)

        # Affichage du carré clignotant
        if square_visible:
            beep_sound.play()
            pygame.draw.rect(window, square_color, (square_x, square_y, square_size, square_size))

    else:  # Si la simulation n'est pas démarrée, afficher le bouton "Démarrer"
        window.fill(BLACK)
        pygame.draw.rect(window, GREEN, start_button)
        start_text = font.render("Démarrer", True, BLACK)
        text_rect = start_text.get_rect(center=start_button.center)
        window.blit(start_text, text_rect)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Pause entre les clignotements
    pygame.time.wait(inter_blink_delay)

# Fermeture de Pygame
pygame.quit()
sys.exit()
