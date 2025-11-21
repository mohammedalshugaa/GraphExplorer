import pygame
import sys
from nodos import Nodo as no

# --- 1. Inicialización de Pygame ---
pygame.init()

# Definición de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configuración de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Círculos al Clic")

# Lista para guardar las posiciones de los círculos (coordenadas x, y)
posiciones_circulos = []
RADIO_CIRCULO = 20
nodo0 = no(1, "cacho", 100, 200)

# --- 2. Bucle Principal del Juego ---
ejecutando = True
while ejecutando:
    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Si el usuario hace clic en el botón de cerrar
            ejecutando = False
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Si se detecta un clic del ratón
            # evento.pos contiene las coordenadas (x, y) del clic
            pos_x, pos_y = evento.pos
            posiciones_circulos.append((pos_x, pos_y))
            # Opcional: imprimir las coordenadas
            print(f"Clic en: ({pos_x}, {pos_y})")

    # --- 3. Lógica del Juego (No necesaria en este caso) ---
    # Aquí iría cualquier actualización de estado si la hubiera

    # --- 4. Dibujo ---
    # a) Rellenar la pantalla con un color de fondo (Blanco)
    pantalla.fill(BLANCO)

    # b) Dibujar todos los círculos guardados
    for posicion in posiciones_circulos:
        # Dibujar un círculo: (superficie, color, centro, radio)
        #pygame.draw.circle(pantalla, AZUL, posicion, RADIO_CIRCULO)
        nodo0.dibujar_nodo(pantalla, AZUL, posicion, nodo0.radio)
        nodo0.pos_x = posicion[0]
        nodo0.pos_y = posicion[1]
        print(nodo0)
        
    # c) Actualizar la pantalla (mostrar lo que se ha dibujado)
    pygame.display.flip()

# --- 5. Salir de Pygame ---
pygame.quit()
sys.exit()