
 
# IMPORTACIONES
import pygame
import sys
import pygame_gui
import ctypes
from   random import randint
import numpy as np
import random
import copy



pygame.init()
window = pygame.display.set_mode((1080, 800), pygame.RESIZABLE)
pygame.display.set_caption("Dijkstra Ventana Maximizada (nativa) con pygame_gui")
SDL_WINDOWPOS_CENTERED = 0x2FFF0000
sdl_window = pygame.display.get_wm_info()['window']
ctypes.windll.user32.ShowWindow(sdl_window, 3)  
window_size = window.get_size()
manager = pygame_gui.UIManager(window_size, r"C:\Users\alshu\Desktop\Grafos\Pygame\Theme.json")





# Dubaimedium, dubairegular, centurygothicnegrita, tahoma, microsoftsansserif, segoeuisemibold
fuente = pygame.font.SysFont("tahoma", 23)
texto = "Hola, este es un cuadro de diálogo en Pygame."
BLANCO      = (255, 255, 255)
GRIS_CLARO  = (230, 230, 230)
GRIS        = (170, 170, 170)
GRIS_OSCURO = (100, 100, 100)
NEGRO       = (0,   0,   0)
AZUL        = (50,  125, 255)

PaleGreen  = (152, 251, 152)
ForestGreen = (34, 139, 34)

MediumAquaMarine = (102, 205, 170)
LightSkyBlue = (135, 206, 250)
Turquoise = (64, 224, 208)

Moccasin = (255, 228, 181)
LightSalmon = (255, 160, 122)
Gold = (255, 215, 0) 

Violet = (238, 130, 238)
SlateBlue  = (106, 90, 205)
HotPink = (255, 105, 180)

Sienna = (160, 82, 45)


miscolores =  [PaleGreen,ForestGreen,MediumAquaMarine,LightSkyBlue,Turquoise,Moccasin,LightSalmon,Gold,Violet,SlateBlue,HotPink,Sienna]






print(pygame.font.get_fonts())



# Estructuras de datos
#n_verts = random.randint(5,15)
n_verts = 10

nodos = []
arcos = []
inodo = 1 
nodo_seleccionado = None
arrastrando = False
min_dist = 20









# Área de los tabs (parte derecha)
panel_rect  = pygame.Rect(1046, 20, 450, 754)
panel_canvas = pygame.Rect(20, 20, 1000, 753)

# Tabs
tabs = {
    "Crear grafo": pygame.Rect(1046, 20, 150, 40),
    "Algoritmos": pygame.Rect(1196, 20, 150, 40),
    "Propiedades": pygame.Rect(1346, 20, 150, 40),
}

tab_activa = "Crear grafo"


# Botón (para Propiedades)
boton_rect = pygame.Rect(1200, 200, 150, 50)



texto_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((1011, 120), (450, 40)),
    text="Este es un programa que muestra grafos.",
    manager=manager
)


botongui         = pygame_gui.elements.UIButton(
        relative_rect = pygame.Rect((1050, 80), (150, 40)),
        text          = 'Grafo aleatorio',
        manager       = manager,
        object_id="#boton_ejemplo")


botoncaptura         = pygame_gui.elements.UIButton(
        relative_rect = pygame.Rect((1050, 120), (150, 40)),
        text          = 'Guardar grafo',
        manager       = manager,
        object_id="#boton_ejemplo")

boton_dijkstra         = pygame_gui.elements.UIButton(
        relative_rect = pygame.Rect((1050, 80), (150, 40)),
        text          = 'dijkstra',
        manager       = manager,
        object_id="#dijkstra")








def captura():
# Definir un área (x, y, ancho, alto)
    area = pygame.Rect(20, 20, 1000, 753)
    # Crear una subsuperficie a partir del área
    subimagen = window.subsurface(area)
    copia = window.subsurface(area).copy()
    # Guardar la imagen recortada
    pygame.image.save(subimagen, "Grafo222.png")


def generar_nodos_no_solapados():
    global inodo, nodos
    nodos.clear()
    inodo = 1
    min_dist = 20  # Distancia mínima entre nodos
    

    for i in range(n_verts):
        while True:
            global colort
            colort = random.choice(miscolores)
            tx, ty = random.randint(55, 980), random.randint(55, 740)

            # Verificar distancia con nodos anteriores
            too_close = False
            for _, x_prev, y_prev, _ in nodos:
                dist = ((tx - x_prev)**2 + (ty - y_prev)**2) ** 0.5
                if dist < min_dist:
                    too_close = True
                    break

            if not too_close:
                nodos.append([inodo, tx, ty, colort])
                inodo += 1
                break

def grafo_alea_no_conexo():
    inodo = 1
    arcos.clear()
    
    
    generar_nodos_no_solapados()
    
    """
    # Generar arcos fijos
    for ar in range(n_arcos):
        nodo1 = random.randint(0, n_verts - 1)
        nodo2 = random.randint(0, n_verts - 1)
        while nodo2 == nodo1 and len(nodos) > 1:
            nodo2 = random.randint(0, n_verts - 1)
        arcos.append((ar, nodo1, nodo2))
    """
    
    for nnodo in range(n_verts):
        for n_conex_nodo in range(1, 2):
            global n_arcos
            n_arcos = 0
            n_arcos += 1
            lista_exlu = copy.deepcopy(nodos)
            del lista_exlu[nnodo]
            global segundo_nodo
            segundo_nodo = random.choice(lista_exlu)
            arcos.append((n_arcos, nnodo, segundo_nodo[0]))
    
    
    
    
    
    
    


    print("los nodos:", nodos)
    



reloj = pygame.time.Clock()
# Reloj para controlar el framerate
running = True

while True:
    
    tiempo = reloj.tick(60) / 1000.0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Detectar clic en pestañas
            for nombre, rect in tabs.items():
                if rect.collidepoint(evento.pos):
                    tab_activa = nombre

        
            if tab_activa == "Propiedades" and boton_rect.collidepoint(evento.pos):
                print("¡Botón presionado!")
        
                            
                            
        if evento.type == pygame_gui.UI_BUTTON_PRESSED:
                    if evento.ui_element == botongui:
                        grafo_alea_no_conexo()  # Llamar a la función
                        
                        
        if evento.type == pygame_gui.UI_BUTTON_PRESSED:
                    if evento.ui_element == botoncaptura:
                        captura()  # Llamar a la función

        
        
        # MOVER LOS NODOS
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo
                # Buscar si se hizo clic sobre un nodo
                for i, (idnodo, x, y, colort) in enumerate(nodos):
                    dx = evento.pos[0] - x
                    dy = evento.pos[1] - y
                    if dx**2 + dy**2 <= 30**2:  # Dentro del radio del nodo
                        nodo_seleccionado = i
                        arrastrando = True
                        break

        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                arrastrando = False
                nodo_seleccionado = None

        elif evento.type == pygame.MOUSEMOTION:
            if arrastrando and nodo_seleccionado is not None:
                # Mover el nodo con el mouse
                _, _, _, _ = nodos[nodo_seleccionado]
                nodos[nodo_seleccionado][1] = max(50, min(evento.pos[0], 1000 - 10))
                nodos[nodo_seleccionado][2] = max(50, min(evento.pos[1], 753 - 10))


        
        
        

        
    # Fondo general
    window.fill(GRIS_CLARO)
    
    
    # Dibujar panel lateral
    pygame.draw.rect(window, GRIS, panel_rect, border_radius=0)
    pygame.draw.rect(window, BLANCO, panel_canvas, border_radius=0)
    

    # Dibujar tabs
    for nombre, rect in tabs.items():
        color = GRIS if tab_activa == nombre else GRIS_OSCURO
        pygame.draw.rect(window, color, rect)
        texto = fuente.render(nombre, True, NEGRO)
        window.blit(texto, (rect.x + 10, rect.y+2))
        
    
    # Contenido del tab seleccionado
    if tab_activa == "Crear grafo":
        pass
        #contenido = fuente.render("Contenido blabla PBIOU&PV", True, NEGRO)
        #window.blit(contenido, (1225, 95))
        
        #pygame.draw.rect(window, GRIS_OSCURO, boton_1, border_radius=0)
        #texto_boton = fuente.render("Random", True, BLANCO)
        #window.blit(texto_boton, (boton_1.x + 35, boton_1.y + 5))

    elif tab_activa == "Algoritmos":
        texto = "Aquí vamos a aplicar algoritmos como dijkstra."
        render = fuente.render(texto, True, NEGRO)
        window.blit(render, (1060, 120))

    elif tab_activa == "Propiedades":
        pygame.draw.rect(window, AZUL, boton_rect, border_radius=10)
        texto_boton = fuente.render("Haz clic", True, BLANCO)
        window.blit(texto_boton, (boton_rect.x + 20, boton_rect.y + 10))
    
    
        
        
    if tab_activa == "Crear grafo":
        botongui.show()
        botoncaptura.show()
        texto_label.show()
        boton_dijkstra.show()
    else:
        botongui.hide()
        botoncaptura.hide()
        texto_label.hide()
        boton_dijkstra.hide()
        
    


    if tab_activa == "Algoritmos":
        boton_dijkstra.show()
    else:
        boton_dijkstra.hide()


        
        
        

    # Dibujar arcos (conexiones fijas)
    for arco in arcos:
        n_arcos, nnodo, segundo_nodo = arco
        pygame.draw.line(window, NEGRO, (nodos[nnodo][1], nodos[nnodo][2]), (nodos[segundo_nodo-1][1], nodos[segundo_nodo-1][2]), 2)
        texto_surface = fuente.render(str(n_arcos), True, NEGRO)
        texto_rect = texto_surface.get_rect(center=(10, n_arcos*20+10))
        window.blit(texto_surface, texto_rect)
    


    
    # Dibujar nodos como círculos
    for inodo, x, y, colort in nodos:
        pygame.draw.circle(window, colort, (x, y), 30)
        texto_surface = fuente.render(str(inodo), True, NEGRO)
        texto_rect = texto_surface.get_rect(center=(x, y))
        window.blit(texto_surface, texto_rect)
    



    




    
    manager.update(tiempo)
    manager.draw_ui(window)
    manager.process_events(evento)
    pygame.display.flip()