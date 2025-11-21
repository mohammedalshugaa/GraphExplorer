
import pygame
import math
import numpy as np
import color_palettes



# La clase principal del programa
class Graph:
    def __init__(self, coor:list, arcos:list, dirigido:bool):
        
        self.coor           = coor
        self.arcos          = arcos
        self.dirigido       = dirigido
        self.es_simple      = True
        self.n_nodos        = len(coor)
        grosor_arco         = 3
        self.grueso_arco    = grosor_arco
        
        
        #print(f"\n numero de los nodos: {len(self.coor)} \n")
        array_coor = np.array(self.coor, dtype=object)              # convertir a un array para mejor visualización
        #print(f"\n Informacion de los nodos: \n {array_coor} \n")
        array_arcos = np.array(self.arcos, dtype=object)            # convertir a un array para mejor visualización
        print(f"\n Informacion de los arcos: \n {array_arcos} \n")
        
        
        # Matrices asociadas al grafo
        self.M_adyacencia   = np.zeros([self.n_nodos, self.n_nodos], dtype=int)
        self.M_pesos        = np.full((self.n_nodos, self.n_nodos), np.inf)
        self.M_conectividad = np.zeros([self.n_nodos, self.n_nodos], dtype=int)
        
        
        
        # Calcular la matriz de adyacencia
        if dirigido == True:
            for origen, destino, bidireccion, _, _, _ in self.arcos:
                self.M_adyacencia[origen][destino] += 1 
                if bidireccion == "bi":
                    self.M_adyacencia[destino][origen] += 1 
        else:
            for origen, destino, _, _, _, _ in self.arcos:
                self.M_adyacencia[origen][destino] += 1
                self.M_adyacencia[destino][origen] += 1 
        print(f"\n Matriz de adyacencia: \n {self.M_adyacencia}")
        
        
        
        
        
    
        # Llenar la matriz de pesos
        if self.es_simple == True:
            if dirigido == True:
                for origen, destino, tipo_arco, peso, _, _ in self.arcos:
                    self.M_pesos[origen][destino] = peso
                    if tipo_arco == "bi":
                        self.M_pesos[destino][origen] = peso  #-1
            else:
                for origen, destino, _, peso, _, _ in self.arcos:
                    self.M_pesos[origen][destino] = peso
                    self.M_pesos[destino][origen] = peso
            
        else:
            if dirigido == True:
                for origen, destino, tipo_arco, peso, _, _ in self.arcos:
                    self.M_pesos[origen][destino] = peso
                    if tipo_arco == "bi":
                        self.M_pesos[destino][origen] = peso # Queda trabajo
            else:
                for origen, destino, _, peso, _, repeticion in self.arcos:
                    if repeticion == 1:
                        self.M_pesos[origen][destino] = peso
                        self.M_pesos[destino][origen] = peso
                    else:
                        pass # Queda trabajo
                        
        
        

            
  
    def es_conexo(self):
        for i in range(1, self.n_nodos):
            self.M_conectividad += np.linalg.matrix_power(self.M_adyacencia, i)
        self.M_conectividad += np.eye(self.n_nodos, dtype=int)
        print(self.M_conectividad)
        
        if 0 in self.M_conectividad:
            print("El grafo NO es conexo")
            return False
        else:
            if self.dirigido == True:
                print("El digrafo es fuertemente conexo")
            else:
                print("El grafo es conexo")
            return True
        
    def convertir_en_conexo(self, color_arco):
        if self.es_conexo() == False:
            for i in range(self.n_nodos):
                for j in range(self.n_nodos):
                    if self.M_conectividad[i][j] == 0:
                        #time.sleep(5)
                        self.arcos.append([i , j, "un", 20, color_arco, 1])
                        print(self.M_conectividad)
                        
    def correccion_por_pendiente(self, m, radio_x=50, radio_y=15):
        # Manejo de pendiente infinita
        if math.isinf(m):
            ang = math.pi / 2
        else:
            ang = math.atan(m)
    
        # Vector perpendicular
        dx = radio_x * math.cos(ang + math.pi / 2)
        dy = radio_y * math.sin(ang + math.pi / 2)
    
        return [abs(int(dx)), abs(int(dy))]
    
    def correccion_por_pendiente_xy(self, x1, y1, x2, y2, radio_x=50, radio_y=25):
        # Ángulo de la línea completa, no solo con la pendiente
        ang = math.atan2(y2 - y1, x2 - x1)
    
        # Ángulo perpendicular
        ang_perp = ang + math.pi / 2
    
        dx = radio_x * math.cos(ang_perp)
        dy = radio_y * math.sin(ang_perp)
        return [abs(int(dx)), abs(int(dy))]

    
    
    


    def dibujar_flecha(self, window, origen, destino, color, RADIUS, linea_inclu):
        #x1, y1 = origen
        #x2, y2 = destino
        x1 = origen[0]
        y1 = origen[1]
        x2 = destino[0]
        y2 = destino[1]

        # Vector entre puntos
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist == 0:
            return  # evitar división por cero

        # Unitarios
        ux = dx / dist
        uy = dy / dist

        # Ajustar puntos para que la flecha no entre al círculo
        start_x = x1 + ux * RADIUS
        start_y = y1 + uy * RADIUS
        end_x = x2 - ux * RADIUS
        end_y = y2 - uy * RADIUS

        # Línea principal
        if linea_inclu == True:
            pygame.draw.line(window, color, (start_x, start_y), (end_x, end_y), self.grueso_arco)
            

        # Punta de flecha
        angle = math.atan2(dy, dx)
        arrow_length = 12
        arrow_width = 6

        left = (end_x - arrow_length * math.cos(angle - math.pi / 6),
            end_y - arrow_length * math.sin(angle - math.pi / 6))
        right = (end_x - arrow_length * math.cos(angle + math.pi / 6),
             end_y - arrow_length * math.sin(angle + math.pi / 6))
        if self.dirigido == True:
            pygame.draw.polygon(window, color, [(end_x, end_y), left, right])     
    
    def distancia(self, p1, p2):
        return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
        
    def pendiente(self, p1, p2):
        if p1[0] == p2[0]:
            return math.inf
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    def definir_p3(self, p1, p2, n_ocurrencias):
        curvatura = -int(self.distancia(p1, p2))/2500 + (5/9)
        mx = (p1[0] + p2[0]) / 2
        my = (p1[1] + p2[1]) / 2

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        length = math.hypot(dx, dy)

        if length == 0:
            return p1

        nx = -dy / length
        ny = dx / length

        p3x = mx + nx * length * curvatura *n_ocurrencias *2
        p3y = my + ny * length * curvatura *n_ocurrencias *2

        return (p3x, p3y)
    
    def quadratic_bezier(self, p1, p2, t, p3):
        x = (1 - t)**2 * p1[0] + 2 * (1 - t) * t * p3[0] + t**2 * p2[0]
        y = (1 - t)**2 * p1[1] + 2 * (1 - t) * t * p3[1] + t**2 * p2[1]
        return (x, y)
    
    def dibujar_curva_con_flecha(self, surface, p1, p2, curva, color_arco, grosor, tamaño_nodo, incluir_linea=True,  n_flechas=1):
        p3 = self.definir_p3(p1, p2, curva)
        grosor = self.grueso_arco
        # Generar puntos de la curva
        raw_points = [self.quadratic_bezier(p1, p2, t / 100, p3) for t in range(101)]

        def longitud(puntos):
            return sum(math.hypot(p2[0]-p1[0], p2[1]-p1[1]) for p1, p2 in zip(puntos, puntos[1:]))

        total_len = longitud(raw_points)

        def recortar_extremos(puntos, radio):
            len_acum = 0
            i_start = 0
            for i in range(1, len(puntos)):
                d = math.hypot(puntos[i][0]-puntos[0][0], puntos[i][1]-puntos[0][1])
                if d >= radio:
                    i_start = i
                    break

            len_acum = 0
            i_end = len(puntos) - 1
            for i in range(len(puntos)-2, -1, -1):
                d = math.hypot(puntos[i][0]-puntos[-1][0], puntos[i][1]-puntos[-1][1])
                if d >= radio:
                    i_end = i
                    break
            return puntos[i_start-1:i_end+2]

        points = recortar_extremos(raw_points, tamaño_nodo)

        # Dibuja la curva
        if incluir_linea and len(points) > 1:
            pygame.draw.lines(surface, color_arco, False, points, grosor)

        def dibujar_flecha_sobre_puntos(p0, p1):
            dx = p1[0] - p0[0]
            dy = p1[1] - p0[1]
            angle = math.atan2(dy, dx)

            arrow_length = 12
            arrow_width = 6

            left = (p1[0] - arrow_length * math.cos(angle - math.pi / 6),
                p1[1] - arrow_length * math.sin(angle - math.pi / 6))
            right = (p1[0] - arrow_length * math.cos(angle + math.pi / 6),
                 p1[1] - arrow_length * math.sin(angle + math.pi / 6))

            pygame.draw.polygon(surface, color_arco, [p1, left, right])

        # Dibujar una o dos flechas
        if len(points) >= 2:
            if n_flechas == 1:
                dibujar_flecha_sobre_puntos(points[-2], points[-1])
            elif n_flechas == 2:
                dibujar_flecha_sobre_puntos(points[-2], points[-1])
                dibujar_flecha_sobre_puntos(points[1], points[0])
 
 
 
 
    # El proceso de dibujo
    def dibujar_dirigido(self, window, color_nodo, color_arco, tamaño_nodo):
            
            font=pygame.font.SysFont('tahoma',  20)

            # Dibujar los arcos
            for arco in self.arcos:
                primer_nodo, segundo_nodo, bidireccion, peso, _, n_ocurrencias = arco
                x1 = self.coor[primer_nodo][0]
                y1 = self.coor[primer_nodo][1]
                x2 = self.coor[segundo_nodo][0]
                y2 = self.coor[segundo_nodo][1]
                
                #m = self.pendiente([x1, y1], [x2, y2])
                #cor = self.correccion_por_pendiente(m, radio_x=50, radio_y=25)
                col = self.correccion_por_pendiente_xy(x1, y1, x2, y2, radio_x=50, radio_y=25)
                if primer_nodo != segundo_nodo:
                    pass
                    #x2, y2 = self.coor[segundo_nodo][:2]
                    #text_surface = font.render(str(peso), antialias=True, color=(0, 0, 0))
                    #window.blit(text_surface, dest=(int((x1+x2)/2)-col[0], int((y1+y2)/2)-col[1]))
                
                if n_ocurrencias == 1:
                    if self.dirigido:
                        self.dibujar_flecha(window, (x1,y1), (x2, y2), color_arco, tamaño_nodo, True)
                        if bidireccion == "bi":
                            self.dibujar_flecha(window, (x2, y2), (x1,y1), color_arco, tamaño_nodo, True)
                    else:
                        #pygame.draw.line(window, color_arco, self.coor[primer_nodo-1], self.coor[segundo_nodo-1], self.grueso_arco)
                        pygame.draw.line(window, color_arco, (x1, y1), (x2, y2), self.grueso_arco)
                        if bidireccion == "bi":
                            pygame.draw.line(window, color_arco, (x2, y2), (x1, y1), self.grueso_arco)
                else:
                    p1 = self.coor[primer_nodo-1]
                    p2 = self.coor[segundo_nodo-1]
                    d = self.distancia(p1, p2)
                    #curvatura = max(0.02, min(0.12, 60 / (d + 1)))
                    curvatura = max(0.04, min(0.13, 70 / (d + 1)))




                    #curvatura = -int(self.distancia(p1, p2))/1000 + (2/9)

                    if self.dirigido:
                        self.dibujar_curva_con_flecha(window, p1, p2, n_ocurrencias * curvatura, color_arco, 3, tamaño_nodo, True)
                        if bidireccion == "bi":
                            #self.dibujar_curva_con_flecha(window, p2, p1, n_ocurrencias * curvatura * 0.7, color_arco, 3, tamaño_nodo, True)
                            self.dibujar_curva_con_flecha(window, p1, p2, n_ocurrencias * curvatura , color_arco, 3, tamaño_nodo, incluir_linea=True,  n_flechas=2)
                    else:
                        points = [self.quadratic_bezier(p1, p2, t / 100, self.definir_p3(p1, p2, n_ocurrencias * curvatura * 0.7)) for t in range(101)]
                        pygame.draw.lines(window, color_arco, False, points, self.grueso_arco)
                        if bidireccion == "bi":
                                points_reverse = [self.quadratic_bezier(p2, p1, t / 100, self.definir_p3(p2, p1, n_ocurrencias * curvatura * 0.7)) for t in range(101)]
                                pygame.draw.lines(window, color_arco, False, points_reverse, self.grueso_arco)

                  
            
            # Dibujar el nodo reflexivo  
            for arco in self.arcos:
                primer_nodo, segundo_nodo, bidireccion, peso, _, _ = arco
                x = self.coor[segundo_nodo][0]
                y = self.coor[segundo_nodo][1]
                coord_flex = [0, 0]
                
                text_surface = font.render(str(peso), antialias=True, color=(0, 0, 0))
                if primer_nodo == segundo_nodo:
                    if  20< x <520  and 20< y <396.5:
                        coord_flex = [x-1.2*tamaño_nodo, y-1.2*tamaño_nodo]
                        pygame.draw.circle(window, color_arco, coord_flex, tamaño_nodo*1, self.grueso_arco)
                    elif  520< x <1020 and 20< y <396.5 :
                        coord_flex = [x+1.2*tamaño_nodo, y-1.2*tamaño_nodo]
                        pygame.draw.circle(window, color_arco, coord_flex, tamaño_nodo*1, self.grueso_arco)
                    elif  20< x <520  and 396.5< y <773:
                        coord_flex = [x-1.2*tamaño_nodo, y+1.2*tamaño_nodo]
                        pygame.draw.circle(window, color_arco, coord_flex, tamaño_nodo*1, self.grueso_arco)
                    else:
                        coord_flex = [x+1.2*tamaño_nodo, y+1.2*tamaño_nodo]
                        pygame.draw.circle(window, color_arco, coord_flex, tamaño_nodo*1, self.grueso_arco)
                window.blit(text_surface, dest=(coord_flex[0]-10, coord_flex[1]-10))
                        
            ### ### ###
            # Dibujar los nodos
            for nodo in self.coor:
                x, y, i, color_nodo, t_nodo, _, _ = nodo
                tamaño_nodo = t_nodo
                pygame.draw.circle(window, color_palettes.NEGRO, (int(self.coor[i][0]), int(self.coor[i][1])), tamaño_nodo+0) 
                pygame.draw.circle(window, color_nodo, (int(self.coor[i][0]), int(self.coor[i][1])), tamaño_nodo)
                
                text_surface = font.render(str(i), antialias=True, color=(0, 0, 0))
                window.blit(text_surface, dest=(x-8,y-12))


                
           
            # Dibujar las flechas del nodo reflexivo  
            for arco in self.arcos:
                primer_nodo, segundo_nodo, bidireccion, _, _, _ = arco
                x = self.coor[segundo_nodo][0]
                y = self.coor[segundo_nodo][1]
                if primer_nodo == segundo_nodo:  
                    if  20< x <520  and 20< y <396.5:
                        self.dibujar_flecha(window, [x-5*tamaño_nodo, y], [x+0.2*tamaño_nodo, y-0.35*tamaño_nodo], color_arco, tamaño_nodo, False)
                    elif  520< x <1020 and 20< y <396.5 :
                        self.dibujar_flecha(window, [x+5*tamaño_nodo, y], [x-0.2*tamaño_nodo, y-0.35*tamaño_nodo], color_arco, tamaño_nodo, False)
                    elif  20< x <520  and 396.5< y <773:
                         self.dibujar_flecha(window, [x-5*tamaño_nodo, y], [x+0.2*tamaño_nodo, y+0.35*tamaño_nodo], color_arco, tamaño_nodo, False)
                    else:
                        self.dibujar_flecha(window, [x+5*tamaño_nodo, y], [x-0.2*tamaño_nodo, y+0.35*tamaño_nodo], color_arco, tamaño_nodo, False)
            
            
            
            # Dibujar las flechas del nodo reflexivo  
            for arco in self.arcos:
                primer_nodo, segundo_nodo, bidireccion, peso, _, _ = arco
                x1 = self.coor[primer_nodo][0]
                y1 = self.coor[primer_nodo][1]
                x2 = self.coor[segundo_nodo][0]
                y2 = self.coor[segundo_nodo][1]
                #font=pygame.font.SysFont('tahoma',  20)
                #text_surface = font.render(str(peso), antialias=True, color=(0, 0, 0))
                #window.blit(text_surface, dest=(int((x1+x2)/2)+5, int((y1+y2)/2)+5))
   
         

        


        

        
        
        
  # funciones no necesarias
    def hay_un_camino_k(self, nombre1, nombre2):
        pass


    def __str__(self):
        return f"Este es un grafo con {self.n_nodos} vertices"


    

class Nodo:
    def __init__(self, coor, arcos):
        self.numero = 1
        self.nombre = 1
        
        self.coor_x = 1
        self.coor_y = 1
        
        self.tamaño = 30
        self.grosor_borde = 0
        
        self.color = 1
        self.color_borde = 1
        
        self.grado_total = 1
        
        self.es_vecino_de= 1
        self.a_que_nodos_llega = 1
        
        
        
        # dirigido
        self.grado_entrada = 1
        self.grado_salida = 1
        
        
        
        
class Arco:
    def __init__(self):
        self.numero = 1
        self.nombre = 1
        
        
        



# utilidades:
# print(p1.M_adyacencia.transpose())
