import pygame
import sys

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pygame Tabs")
fuente = pygame.font.SysFont("Arial", 30)

# Colores
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
GRIS_OSCURO = (150, 150, 150)
NEGRO = (0, 0, 0)

# Estado de pestaña activa
tab_activa = "Inicio"

# Botones de pestaña (x, y, ancho, alto, nombre)
tabs = {
    "Inicio": pygame.Rect(50, 20, 150, 40),
    "Opciones": pygame.Rect(220, 20, 150, 40),
    "Acerca de": pygame.Rect(390, 20, 150, 40),
}

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for nombre, rect in tabs.items():
                if rect.collidepoint(evento.pos):
                    tab_activa = nombre

    pantalla.fill(BLANCO)

    # Dibujar las pestañas
    for nombre, rect in tabs.items():
        color = GRIS_OSCURO if tab_activa == nombre else GRIS
        pygame.draw.rect(pantalla, color, rect)
        texto = fuente.render(nombre, True, NEGRO)
        pantalla.blit(texto, (rect.x + 10, rect.y + 5))

    # Dibujar contenido según pestaña activa
    if tab_activa == "Inicio":
        contenido = "Bienvenido a la pantalla de inicio"
    elif tab_activa == "Opciones":
        contenido = "Aquí puedes configurar el juego"
    elif tab_activa == "Acerca de":
        contenido = "Este juego fue hecho con Pygame"

    texto_contenido = fuente.render(contenido, True, NEGRO)
    pantalla.blit(texto_contenido, (50, 100))

    pygame.display.flip()
    
    
    
    
    # Definir un área (x, y, ancho, alto)
    area = pygame.Rect(100, 100, 200, 150)

    # Crear una subsuperficie a partir del área
    subimagen = pantalla.subsurface(area)
    copia = pantalla.subsurface(area).copy()
    # Guardar la imagen recortada
    pygame.image.save(subimagen, "captura_recorte.png")






    reloj.tick(60)

