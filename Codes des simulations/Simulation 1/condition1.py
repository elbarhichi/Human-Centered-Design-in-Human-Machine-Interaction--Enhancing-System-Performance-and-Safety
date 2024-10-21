import pygame
import sys
import math


'''
Ecrire la fréquence cardiaque en battements par minute (BPM) dans la variable f
'''

# Fréquence cardiaque en battements par minute (BPM)
f = 100

# Fréquence cardiaque en battements par seconde (BPS)
fs = f / 60

# Période d'un battement en secondes (Ts)
Ts = 1 / fs

# Durée totale du mouvement de la bille en secondes
total_duration = 29

# Calcul du nombre de va-et-vient
number_of_cycles = math.ceil(total_duration / Ts)

print("Nombre de va-et-vient:", number_of_cycles)

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
pygame.display.set_caption("Simulation de la bille")

# Définition des propriétés de la bille
BALL_SIZE = 20
BALL_COLOR = WHITE
ball_x = BALL_SIZE  # Position initiale de la balle ajustée pour tenir compte du bouton
ball_y = WINDOW_HEIGHT // 2

# Calcul de la vitesse de la bille en pixels par seconde
ball_speed_x = (number_of_cycles * 2 * (WINDOW_WIDTH - BALL_SIZE * 2)) / total_duration

# Chargement des images
image1 = pygame.image.load("image1.jpg")
image2 = pygame.image.load("image2.jpg")
image3 = pygame.image.load("image3.jpg")

# Position des images en haut à droite
image_position = (100, 40 )

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
cycles_count = 0  # Compteur de va-et-vient
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if start_button.collidepoint(mouse_pos):
                simulation_started = True
                start_time = pygame.time.get_ticks()  # Enregistrement du moment du clic

    # Si la simulation a démarré
    if simulation_started:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  # Démarrage du mouvement après 1 seconde
            ball_x += ball_speed_x / 60
            if ball_x <= BALL_SIZE or ball_x >= WINDOW_WIDTH - BALL_SIZE:
                ball_speed_x *= -1
                cycles_count += 1  # Incrémentation du compteur de va-et-vient

            # Vérification si le nombre de va-et-vient prévu est atteint
            if cycles_count >= number_of_cycles * 2:
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
    
    # Dessin de la bille
    pygame.draw.circle(window, BALL_COLOR, (ball_x, ball_y), BALL_SIZE)

    # Dessin du bouton "Démarrer" si visible
    if start_button_visible:
        pygame.draw.rect(window, GREEN, start_button)
        start_text = font.render("Démarrer", True, BLACK)
        text_rect = start_text.get_rect(center=start_button.center)
        window.blit(start_text, text_rect)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Gestion de la disparition du bouton "Démarrer"
    if simulation_started and start_button_visible:
        start_button_visible = False

    # Limite de vitesse de rafraîchissement
    pygame.time.Clock().tick(60)

# Fermeture de Pygame
pygame.quit()
sys.exit()
