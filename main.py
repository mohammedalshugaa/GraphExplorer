
# Importaciones
import pygame
import pygame_gui
import sys
import ctypes
from   datetime     import datetime
import color_palettes as clrs

import nodos as no
import arcos as ar
import grafos as gr


# Inicialización del programa
pygame.init()
window = pygame.display.set_mode((1080, 800), pygame.RESIZABLE)
pygame.display.set_caption("Grafos v2")
SDL_WINDOWPOS_CENTERED = 0x2FFF0000
sdl_window = pygame.display.get_wm_info()['window']
ctypes.windll.user32.ShowWindow(sdl_window, 3)  
window_size = window.get_size()
manager = pygame_gui.UIManager(window_size) 
print("dimension de la ventana", window_size)
font=pygame.font.SysFont('tahoma',  30)



# Inicializacion de canvas y panel
x_canvas = int(window_size[0]*6.8/10)
x_panel = window_size[0]-x_canvas
y_todo = window_size[1]
canvas = pygame.Rect(0, 0, x_canvas, y_todo)
panel  = pygame.Rect(x_canvas, 0, x_panel, y_todo)




# crear arco
# c dirigido o no: radio
# c color arco: color picker o paleta
# c grosor arco: slider o entrada
# c tamaño y color flecha: slider + picker o paleta 
# c peso: entrada
# c direccion de arco: radio?
# c repeticion?
# borrar arco





nodo0 = no.Nodo(1, "cacho", 100, 200, borde=3)
nodo1 = no.Nodo(2, "cacho", 200, 550)
nodo2 = no.Nodo(3, "cacho", 350, 570)
nodos_1 = [nodo0, nodo1, nodo2]  

arco_1 = ar.ArcoNoDirigido(nodos_1, 1, "archi", nodo0, nodo1, peso=12)

miprg = gr.GrafoNoDirigido("mi_primer_grafo")
miprg.agregar_nodo(nodo0)
miprg.agregar_nodo(nodo1)
miprg.agregar_nodo(nodo2)
print(miprg)




reloj = pygame.time.Clock()
running = True
while True:
    
    tiempo = reloj.tick(60) / 1000.0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
        
    # Fondo del programa
    window.fill(clrs.GRIS) 
    pygame.draw.rect(window, clrs.BLANCO, canvas, border_radius=0)
    

    
    # Dibujar todo ???
    pygame.draw.rect(window, clrs.GRIS, panel, border_radius=0)

    miprg.dibujar_grafo(window)
        


    
    manager.update(tiempo)
    manager.draw_ui(window)
    manager.process_events(evento)
    pygame.display.flip()
    